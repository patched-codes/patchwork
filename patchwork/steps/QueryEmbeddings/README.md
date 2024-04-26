## QueryEmbeddings.py

### Inputs:
- `inputs`: A dictionary containing keys "embedding_name" and "texts", and optional keys "top_k" and "token_limit".

### Outputs:
- `embedding_results`: A list of dictionaries containing document details and distances, sorted by distance.

### Code:
- Imports necessary modules from the project.
- Defines a class `QueryEmbeddings` inheriting from `Step`.
- Initializes the class with input data, identifies required keys, and sets up connection to a database.
- Executes a query on input texts, filters results based on token count and distance.
- Returns a sorted list of document details and distances based on the query results.

This code seems to be a part of a larger project involving querying embeddings of texts and returning relevant information based on the query results.