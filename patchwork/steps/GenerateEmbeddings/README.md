## `patchwork/steps/GenerateEmbeddings/GenerateEmbeddings.py`

### Inputs:
- `inputs` dictionary with keys `"embedding_name"` and `"documents"`.

### Code:
- Defines `filter_by_extension` function to filter files by extension.
- Defines `split_text` function to chunk text based on given parameters.
- Class `GenerateEmbeddings(Step)` inheriting from `Step`.
- Checks for required keys in the input dictionary.
- Initializes the step with input data and sets up a client connection to a vector database.
- Runs the step by processing documents and embeddings, splitting document texts if needed, and upserting data into the vector database.

### Outputs:
- Returns an empty dictionary.

## `patchwork/steps/GenerateEmbeddings/__init__.py`

- Empty file.