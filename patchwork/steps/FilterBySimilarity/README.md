## Table of Contents

- [patchwork/steps/FilterBySimilarity/typed.py](#patchworkstepsFilterBySimilaritytyped.py)
- [patchwork/steps/FilterBySimilarity/FilterBySimilarity.py](#patchworkstepsFilterBySimilarityFilterBySimilarity.py)
- [patchwork/steps/FilterBySimilarity/__init__.py](#patchworkstepsFilterBySimilarity__init__.py)

## File: patchwork/steps/FilterBySimilarity/typed.py

- Defines input and output types for the `FilterBySimilarity` step.

## File: patchwork/steps/FilterBySimilarity/FilterBySimilarity.py

- Defines a step `FilterBySimilarity` that filters a list of items based on text similarity to keywords.
- Utilizes TF-IDF vectorization and cosine similarity calculations.
- Input: `list`, `keywords` (mandatory), `keys`, `top_k`.
- Output: `result_list` containing items with highest similarity scores to keywords.

## File: patchwork/steps/FilterBySimilarity/__init__.py

- Empty file.