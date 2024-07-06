## Documentation for `PR.py`

### Inputs
- This file defines a class `PR` that inherits from `Step`.
- `PR` class takes `inputs` as a parameter in its constructor.
- It requires specific keys in the `inputs` dictionary mentioned in `required_keys`.
- The keys required in `inputs` are fetched from the `PRInputs` class in the `typed.py` file.
- It relies on other classes such as `CommitChanges`, `CreatePR`, and `PreparePR`.

### Outputs
- The `run` method of the `PR` class returns a dictionary of specific keys with values obtained from the outputs of `CommitChanges`, `PreparePR`, and `CreatePR` classes.
- It employs `exclude_none_dict` to remove `None` values in the returned dictionary.

### Usage
- The `PR` class is used to orchestrate the creation of a PR (Pull Request) by utilizing different steps like committing changes, preparing a PR, and creating a PR.
- `PR` class ensures that the required inputs are provided before proceeding with the PR creation process.