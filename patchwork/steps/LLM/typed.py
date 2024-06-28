from patchwork.steps.CallLLM.typed import CallLLMInputs, CallLLMOutputs
from patchwork.steps.ExtractModelResponse.typed import (
    ExtractModelResponseInputs,
    ExtractModelResponseOutputs,
)
from patchwork.steps.PreparePrompt.typed import (
    PreparePromptInputs,
    PreparePromptOutputs,
)


class LLMInputs(PreparePromptInputs, CallLLMInputs, ExtractModelResponseInputs):
    pass


class LLMOutputs(PreparePromptOutputs, CallLLMOutputs, ExtractModelResponseOutputs):
    pass
