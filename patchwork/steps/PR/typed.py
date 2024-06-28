from patchwork.steps.CommitChanges.typed import (
    CommitChangesInputs,
    CommitChangesOutputs,
)
from patchwork.steps.CreatePR.typed import CreatePRInputs, CreatePROutputs
from patchwork.steps.PreparePR.typed import PreparePRInputs, PreparePROutputs


class PRInputs(CommitChangesInputs, PreparePRInputs, CreatePRInputs):
    pass


class PROutputs(CommitChangesOutputs, PreparePROutputs, CreatePROutputs):
    pass
