from __future__ import annotations

from patchwork.common.utils.dependency import chromadb
from patchwork.common.utils.utils import (
    count_openai_tokens,
    get_embedding_function,
    get_vector_db_path,
)
from patchwork.logger import logger
from patchwork.step import Step


class QueryEmbeddings(Step):
    required_keys = {"embedding_name", "texts"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        client = chromadb().PersistentClient(path=get_vector_db_path())
        embedding_function = get_embedding_function(inputs)
        self.collection = client.get_collection(name=inputs["embedding_name"], embedding_function=embedding_function)

        self.texts: list[str] = inputs["texts"]
        self.top_k = inputs.get("top_k", 10)
        self.token_limit = inputs.get("token_limit", 4096)

    def run(self):
        results = self.collection.query(
            query_texts=self.texts, n_results=self.top_k, include=["metadatas", "distances"]
        )

        token_count = 0
        embedding_results_by_id = {}
        for i in range(len(results["ids"])):
            for j in range(len(results["ids"][i])):
                metadata = results["metadatas"][i][j]
                distance = results["distances"][i][j]

                if metadata["original_document"] is None:
                    continue
                if metadata["original_id"] in embedding_results_by_id:
                    if distance < embedding_results_by_id[metadata["original_id"]]["distance"]:
                        embedding_results_by_id[metadata["original_id"]]["distance"] = distance
                    continue

                token_count += count_openai_tokens(metadata["original_document"])
                if token_count > self.token_limit:
                    break

                original_metadatas = {
                    key: value
                    for key, value in metadata.items()
                    if key not in ["id", "document", "distance", "original_document", "original_id"]
                }
                embedding_results_by_id[metadata["original_id"]] = dict(
                    id=metadata["original_id"],
                    document=metadata["original_document"],
                    distance=distance,
                    **original_metadatas,
                )

            if token_count > self.token_limit:
                break

        return dict(embedding_results=list(sorted(embedding_results_by_id.values(), key=lambda x: x["distance"])))
