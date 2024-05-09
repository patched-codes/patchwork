import pytest

from patchwork.steps.GenerateEmbeddings.GenerateEmbeddings import (
    GenerateEmbeddings,
    filter_by_extension,
)


def test_filter_by_extension(tmp_path):
    assert filter_by_extension("example.txt", [".txt"])
    assert not filter_by_extension("example.txt", [".pdf"])


def test_generate_embeddings_init():
    inputs = {"embedding_name": "test", "documents": [{"document": "test document"}]}
    step = GenerateEmbeddings(inputs)
    assert step.collection is not None
    assert step.documents == inputs["documents"]


def test_generate_embeddings_run():
    inputs = {"embedding_name": "test", "documents": [{"document": "test document"}]}
    step = GenerateEmbeddings(inputs)
    result = step.run()
    assert result == {}


def test_generate_embeddings_init_required_keys_missing():
    inputs = {"documents": [{"document": "test document"}]}
    with pytest.raises(ValueError):
        GenerateEmbeddings(inputs)


def test_generate_embeddings_init_embedding_name_missing():
    inputs = {"embedding_name": "test"}
    with pytest.raises(ValueError):
        GenerateEmbeddings(inputs)


def test_generate_embeddings_run():
    inputs = {"embedding_name": "test", "documents": [{"document": "test document"}]}
    step = GenerateEmbeddings(inputs)
    result = step.run()
    assert result == {}
