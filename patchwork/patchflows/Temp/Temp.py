from datetime import datetime
import os

from patchwork.step import Step
from patchwork.steps import BrowserUse
from typing import Tuple, List

upi_url = "https://10.142.27.8/UPI/login"
m2p_url = "http://qa-jiocbs.m2pfintech.dev/dashboard/login"
files: List[Tuple[str, List[str]]] = [("POS Settlement", []), ("IMPS Settlement", []), ("Wallet Transactions", [])]
end_of_task = "Then leave the rest for the user. Your job is done."


browser_use_defaults = dict(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    generate_gif=True,
    headless=False,
    task_value={},
)


def create_inputs(task: str, **kwargs):
    cloned_dict = browser_use_defaults.copy()
    cloned_dict.update(**kwargs)
    cloned_dict["task"] = task + "\n" + end_of_task
    return cloned_dict


class Temp(Step):
    def run(self):
        date = datetime.now().strftime("%d-%b-%Y")
        os.makedirs(f"tmp/working_files/{date}", exist_ok=True)
        for file_type in ["Raw Data", "Merchant Raw Data", "PSP Raw data"]:
            BrowserUse(
                create_inputs(
                    task=f"""
Go to {upi_url}
Login using username `9167471523` and password `Patched#1901`

Click on File Download
Click on Settlement Files Download

In From date enter {date}, and in To date enter {date}
In Cycle Name select All
Select File Type {file_type} and click on 'File Search'.
It will give you 10 files. Click on the download button of each file.
"""
                )
            ).run()

        return {}
