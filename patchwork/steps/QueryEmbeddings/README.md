# Documentation for `QueryEmbeddings.py`

## Inputs
- Module imports:
  - `chromadb`
  - `get_embedding_function` from `patchwork.common.utils.utils`
  - `get_vector_db_path` from `patchwork.common.utils.utils`
- Classes:
  - `QueryEmbeddings` (extending `Step` class)
- Attributes:
  - `required_keys` set to `{"embedding_name", "texts"}`
- Methods:
  - `__init__` method taking `inputs` dict as a parameter to initialize the class instance.
  - `run` method to execute the functionality of querying embeddings.

## Outputs
- A dictionary containing the embedded results of the queried texts. The output includes:
  - `embedding_results` key with a value being a sorted list of embedding results by distance.

## Usage
The `QueryEmbeddings` class is designed to query embeddings for a list of texts using a specified embedding function and a given embedding name. 
- Users can pass the required inputs to the `__init__` method to create an instance of `QueryEmbeddings`.
- The `run` method executes the query process and returns the dictionary with the embedding results sorted by distance, respecting the specified token limit.