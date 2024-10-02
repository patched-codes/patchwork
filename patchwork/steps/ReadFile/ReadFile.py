from patchwork.common.utils.utils import open_with_chardet
from patchwork.step import Step
from patchwork.steps.ReadFile.typed import ReadFileInputs


class ReadFile(Step):
    def __init__(self, inputs):
        super().__init__(inputs)
        missing_keys = ReadFileInputs.__required_keys__.difference(inputs.keys())
        if len(missing_keys) > 0:
            raise ValueError(f"Missing required data: {missing_keys}")

        self.file = inputs["file_path"]

    def run(self):
        with open_with_chardet(self.file, "r") as f:
            file_contents = f.read()

        return dict(file_path=self.file, file_content=file_contents)
