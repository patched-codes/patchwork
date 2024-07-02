This documentation provides an overview of three Python files in a project under the `patchwork/steps/LLM/` directory. It includes details on file sizes, creation and modification dates, and the content of the code within them.

### Inputs
The main file, `LLM.py`, defines a class `LLM` that is a part of a this step in the larger patchwork Python package. It has some required inputs defined in `typed.py` that need to be provided while initializing an instance of the `LLM` class.

### Outputs
The `LLM` class has a `run()` method that orchestrates various steps such as preparing prompts, calling language models, and extracting model responses. It outputs different results like prompts used, openAI responses retrieved, and extracted responses from the model.