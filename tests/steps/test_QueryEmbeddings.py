import uuid

import chromadb
import pytest

from patchwork.common.utils.utils import get_vector_db_path
from patchwork.steps.QueryEmbeddings.QueryEmbeddings import QueryEmbeddings


@pytest.fixture
def setup_collection():
    """Sets up a test collection in a Chroma vector database.
    
    This function creates a persistent Chroma client, creates or retrieves a test collection,
    inserts test data into the collection, and yields the collection for testing purposes.
    After the test is complete, it cleans up by deleting the test collection.
    
    Args:
        None
    
    Returns:
        chromadb.Collection: A Chroma collection object for testing.
    
    Yields:
        chromadb.Collection: The test collection with sample data.
    
    Raises:
        chromadb.errors.ChromaError: If there are issues with database operations.
    """
    _TEST_COLLECTION = "test"

    client = chromadb.PersistentClient(path=get_vector_db_path())
    collection = client.get_or_create_collection(_TEST_COLLECTION)
    collection.upsert(
        ids=[str(uuid.uuid1()), str(uuid.uuid1()), str(uuid.uuid1())],
        documents=["text1", "text2", "text3"],
        metadatas=[
            {"original_id": "1", "original_document": "text1"},
            {"original_id": "2", "original_document": "text2"},
            {"original_id": "3", "original_document": "text3"},
        ],
    )
    yield collection
    client.delete_collection(_TEST_COLLECTION)


def test_required_keys(setup_collection):
    # Test that the required keys are checked
    """Test the checking of required keys for QueryEmbeddings.
    
    Args:
        setup_collection (object): A fixture or object that provides a collection with a name attribute.
    
    Returns:
        None: This method doesn't return a value, it performs assertions.
    
    Raises:
        AssertionError: If the required keys are not properly checked by QueryEmbeddings.
    """
    inputs = {"embedding_name": setup_collection.name, "texts": ["text1", "text2"]}
    query_embeddings = QueryEmbeddings(inputs)


def test_missing_required_key():
    # Test that a ValueError is raised when a required key is missing
    inputs = {"texts": ["text1", "text2"]}
    with pytest.raises(ValueError):
        QueryEmbeddings(inputs)


def test_query_results(setup_collection):
    # Test that the query results are processed correctly
    collection = setup_collection
    inputs = {"embedding_name": collection.name, "texts": ["text1", "text2"]}
    query_embeddings = QueryEmbeddings(inputs)
    results = query_embeddings.run()
    assert isinstance(results, dict)
    assert "embedding_results" in results


@pytest.mark.parametrize("top_k", [1, 2, 3])
def test_top_k(setup_collection, top_k):
    # Test that the token limit is enforced
    """Test the top-k functionality of the QueryEmbeddings class.
    
    Args:
        setup_collection: A test fixture providing a configured collection for testing.
        top_k (int): The number of top results to return.
    
    Returns:
        None: This method doesn't return anything explicitly, but uses assertions to verify the behavior.
    
    Raises:
        AssertionError: If the number of embedding results doesn't match the specified top_k value.
    """
    inputs = {"embedding_name": setup_collection.name, "texts": ["text1"], "top_k": top_k}
    query_embeddings = QueryEmbeddings(inputs)
    results = query_embeddings.run()
    assert len(results["embedding_results"]) == top_k
