from collections import defaultdict

import requests
from dataclasses import dataclass

@dataclass
class SonarVuln:
    cwe: str
    bug_msg: str
    start: int
    end: int


class SonarClient:
    __sonar_url = "https://sonarcloud.io/api/"
    __issue_path = "issues/search"
    __hotspot_path = "hotspots/search"
    __hotspot_details_path = "hotspots/show"

    def __init__(self, access_token: str, url: str = __sonar_url) -> None:
        self._access_token = access_token
        self._url = url

    def find_vulns(self, project_key: str) -> dict[str, list[SonarVuln]]:
        rv = defaultdict(list)
        for hotspot in self._find_hotspots(project_key):
            hotspot_details = self._find_hotspot_details(hotspot["key"])
            if hotspot_details is None:
                continue

            path = hotspot_details["component"]["path"]

            vuln = SonarVuln(
                cwe=hotspot_details["rule"]["name"],
                bug_msg=hotspot_details["rule"]["riskDescription"],
                start=hotspot_details["textRange"]["startLine"],
                end=hotspot_details["textRange"]["endLine"],
            )

            rv[path].append(vuln)
        return rv

    def _find_hotspot_details(self, hotspot_key: str) -> dict | None:
        headers = {"Authorization": f"Bearer {self._access_token}"}
        # Define the parameters for Hotspot API request
        params: dict[str, str | int] = {"hotspot": hotspot_key}
        url = self._url + self.__hotspot_details_path
        response = requests.get(url, params=params, headers=headers)
        if not response.ok:
            print("Something went wrong with sonar hotspot details API:", response.text)
            return None

        return response.json()

    def _find_hotspots(self, project_key: str):
        page = 1
        page_size = 50

        headers = {"Authorization": f"Bearer {self._access_token}"}
        # Define the parameters for Hotspot API request
        params: dict[str, str | int] = {"p": page, "ps": page_size, "projectKey": project_key, "status": "TO_REVIEW"}

        url = self._url + self.__hotspot_path

        is_done = False
        while not is_done:
            response = requests.get(url, params=params, headers=headers)
            if not response.ok:
                print("Something went wrong with hotspot API:", response.text)
                return

            data = response.json()
            hotspots = data["hotspots"]

            is_done = len(hotspots) < page_size
            params["p"] = int(params["p"]) + 1

            for hotspot in hotspots:
                yield hotspot
