# Documentation for Patchwork JoinList Step

## Inputs

### `JoinList.py`
- Accepts input data containing a list and a delimiter.
- Checks for missing required keys and raises a `ValueError` if any are missing.

### `typed.py`
- Defines the data types expected for the input list and delimiter.
- Input list is expected to be a list of strings.
- Delimiter is expected to be a string annotated with configuration information.

## Outputs

### `JoinList.py`
- Combines the list elements using the provided delimiter.
- Returns a dictionary with the concatenated text as the output.