from __future__ import annotations

import uuid

from typing_extensions import Any

from patchwork.common.utils.dependency import chromadb
from patchwork.common.utils.utils import get_embedding_function, get_vector_db_path
from patchwork.logger import logger
from patchwork.step import Step


def filter_by_extension(file, extensions):
    return any(file.endswith(ext) for ext in extensions)


def split_text(document_text: str, chunk_size: int, overlap: int) -> list[str]:
    char_length = len(document_text)
    chunks = []
    for i in range(0, char_length, chunk_size - overlap):
        chunk = "".join(document_text[i : i + chunk_size])
        if chunk == "":
            continue

        chunks.append(chunk)

    return chunks


def delete_collection(client, collection_name):
    for collection in client.list_collections():
        if collection.name == collection_name:
            client.delete_collection(collection_name)
            break


class GenerateEmbeddings(Step):
    required_keys = {"embedding_name", "documents"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        client = chromadb().PersistentClient(path=get_vector_db_path())

        if inputs.get("disable_cache", False):
            delete_collection(client, inputs["embedding_name"])

        embedding_function = get_embedding_function(inputs)
        self.collection = client.get_or_create_collection(
            inputs["embedding_name"], embedding_function=embedding_function, metadata={"hnsw:space": "cosine"}
        )
        self.documents: list[dict[str, Any]] = inputs["documents"]

        self.chunk_size = inputs.get("chunk_size", 4000)
        self.overlap_size = inputs.get("overlap_size", 2000)

    def run(self) -> dict:
        document_ids = []
        documents = []
        document_metadatas = []

        embedding_ids = []
        embeddings = []
        embedding_metadatas = []
        for document in self.documents:
            document_text = document.get("document")
            embedding = document.get("embedding")

            if document_text is not None:
                doc_id = str(document.get("id"))
                document_texts = split_text(document_text, self.chunk_size, self.overlap_size)
                for i, document_text in enumerate(document_texts):
                    document_ids.append(str(uuid.uuid4()))
                    documents.append(document_text)

                    metadata = {key: value for key, value in document.items() if key not in ["id", "document"]}
                    metadata["original_document"] = document_text
                    metadata["original_id"] = doc_id
                    document_metadatas.append(metadata)
            elif embeddings is not None:
                embedding_ids.append(str(document.get("id")))
                embeddings.append(embedding)

                metadata = {key: value for key, value in document.items() if key not in ["embedding"]}
                embedding_metadatas.append(metadata)

        if len(document_ids) > 0:
            self.collection.upsert(ids=document_ids, documents=documents, metadatas=document_metadatas)
        if len(embedding_ids) > 0:
            self.collection.upsert(ids=embedding_ids, embeddings=embeddings, metadatas=embedding_metadatas)

        return dict()
