# Code Documentation

## Input
- This code is part of the Patchwork package and implements the `ScanSonar` step.
- The `ScanSonar` class requires the following inputs in its initialization:
  - `sonarqube_project_key` (required): The SonarQube project identifier
  - `sonarqube_access_token` (required): Authentication token for SonarQube API access
  - `sonarqube_base_url` (required): SonarQube instance URL (e.g., https://sonarcloud.io)

## Output
- The `ScanSonar` class has a `run` function that collects vulnerability information from SonarQube.
- Returns a dictionary with a `files_to_patch` key containing a list of `SonarVulnerability` objects.
- Each `SonarVulnerability` contains:
  - `uri`: File path where the vulnerability was found
  - `startLine`: Starting line of the vulnerability
  - `endLine`: Ending line of the vulnerability
  - `cwe`: Common Weakness Enumeration identifier
  - `description`: Detailed description of the vulnerability

## Dependencies
- Requires the SonarQube API to be accessible
- Uses the internal `SonarClient` for API communication
- Authentication via access token is required
