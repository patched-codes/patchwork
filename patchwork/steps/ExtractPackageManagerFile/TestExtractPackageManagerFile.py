import tempfile
import unittest
from pathlib import Path

from patchwork.steps.ExtractPackageManagerFile.ExtractPackageManagerFile import (
    ExtractPackageManagerFile,
)


class TestExtractPackageManagerFile(unittest.TestCase):
    def test_run(self):
        # Content of a SBOM VDR file
        sbom_vdr_file_content = """{
        "components": [
        {
            "group": "",
            "name": "jquery",
            "version": "3.0.0-alpha1",
            "hashes": [
                {
                    "alg": "SHA-512",
                    "content": "6a0087901dd1b4f6333e27c74583eec40a16157fadd3d56d24a0333ce8d4bedb3faaae4fff54942c46dda18f21154492dde4d8ff4dc232549f691022a744f7e8"
                }
            ],
            "purl": "pkg:npm/jquery@3.0.0-alpha1",
            "type": "framework",
            "bom-ref": "pkg:npm/jquery@3.0.0-alpha1",
            "properties": [
                {
                    "name": "SrcFile",
                    "value": "/Users/user/Documents/GitHub/example-javascript/package-lock.json"
                },
                {
                    "name": "ResolvedUrl",
                    "value": "https://registry.npmjs.org/jquery/-/jquery-3.0.0-alpha1.tgz"
                },
                {
                    "name": "LocalNodeModulesPath",
                    "value": "node_modules/jquery"
                }
            ]
        }
    ],
    "vulnerabilities": [
        {
            "bom-ref": "CVE-2015-9251/pkg:npm/jquery@3.0.0-alpha1",
            "id": "CVE-2015-9251",
            "source": {
                "name": "NVD",
                "url": "https://nvd.nist.gov/vuln/detail/CVE-2015-9251"
            },
            "ratings": [
                {
                    "score": 6.1,
                    "severity": "medium",
                    "vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N",
                    "method": "CVSSv3"
                }
            ],
            "cwes": [
                79
            ],
            "description": "# Cross-Site Scripting (XSS) in jquery\\nAffected versions of `jquery` interpret `text/javascript` responses from cross-origin ajax requests, and automatically execute the contents in `jQuery.globalEval`, even when the ajax request doesn't contain the `dataType` option.\\n\\n\\n## Recommendation\\n\\nUpdate to version 3.0.0 or later.",
            "recommendation": "Update to 3.5.0 or later",
            "advisories": [
                {
                    "title": "other",
                    "url": "http://packetstormsecurity.com/files/156743/OctoberCMS-Insecure-Dependencies.html"
                },
                {
                    "title": "GitHub Issue",
                    "url": "https://github.com/jquery/jquery/issues/2432#issuecomment-403761229"
                },
                {
                    "title": "GitHub PR",
                    "url": "https://github.com/jquery/jquery/pull/2588/commits/c254d308a7d3f1eac4d0b42837804cfffcba4bb2"
                },
                {
                    "title": "vendor",
                    "url": "http://www.oracle.com/technetwork/security-advisory/cpuoct2018-4428296.html"
                },
                {
                    "title": "exploit",
                    "url": "http://seclists.org/fulldisclosure/2019/May/13"
                },
                {
                    "title": "Mailing List",
                    "url": "http://lists.opensuse.org/opensuse-security-announce/2020-03/msg00041.html"
                }
            ],
            "analysis": {
                "state": "exploitable",
                "detail": "See http://seclists.org/fulldisclosure/2019/May/13"
            },
            "affects": [
                {
                    "ref": "pkg:npm/jquery@3.0.0-alpha1",
                    "versions": [
                        {
                            "version": "3.0.0-alpha1",
                            "status": "affected"
                        },
                        {
                            "version": "3.5.0",
                            "status": "unaffected"
                        }
                    ]
                }
            ],
            "properties": [
                {
                    "name": "depscan:insights",
                    "value": "Indirect dependency\\nVendor Confirmed\\nKnown Exploits"
                },
                {
                    "name": "depscan:prioritized",
                    "value": "true"
                },
                {
                    "name": "affectedVersionRange",
                    "value": "jquery@>=1.12.3-<3.0.0"
                }
            ],
            "published": "2018-01-22T13:32:06",
            "updated": "2024-03-10T05:18:22"
        }
    ]
}"""

        # Create a temporary directory and file
        with tempfile.TemporaryDirectory() as temp_dir:
            sbom_vdr_file_path = Path(temp_dir) / "sbom-universal.vdr.json"
            with open(sbom_vdr_file_path, "w") as f:
                f.write(sbom_vdr_file_content)

            inputs = {}
            inputs.update({"sbom_vdr_file_path": sbom_vdr_file_path})

            # Instantiate and run the ExtractPackageManagerFile step
            result = ExtractPackageManagerFile(inputs).run()

            # Verify the result
            files_to_patch = result.get("files_to_patch")
            self.assertIsNotNone(files_to_patch, "files_to_patch should not be None")


if __name__ == "__main__":
    unittest.main()
