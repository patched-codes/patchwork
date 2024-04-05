import unittest
from pathlib import Path

from patchwork.steps import CallCode2Prompt


class TestCallCode2Prompt(unittest.TestCase):
    def test_run(self):
        inputs = {}
        folder_path = Path.cwd()
        inputs["folder_path"] = folder_path
        result = CallCode2Prompt(inputs).run()
        prompt_content_md = result.get("prompt_content_md")

        # Check that prompt_content_md is not None and not an empty string
        self.assertTrue(prompt_content_md, "The markdown content should not be empty.")


if __name__ == "__main__":
    unittest.main()
