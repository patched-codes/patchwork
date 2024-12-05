# Documentation for CallAPI Step

## Inputs:
- `url (str)`: The URL to make the API call to.
- `method (str)`: The HTTP method to use for the request (GET, POST, PUT, PATCH, DELETE, HEAD).
- `headers (dict)`: Optional. Headers to include in the request.
- `body (dict)`: Optional. The body of the request.

## Outputs:
- `status_code (int)`: The status code of the API response.
- `headers (dict)`: The headers of the API response.
- `body (str)`: The body of the API response.

The `CallAPI` class extends `Step` and is used to make API calls using the `requests` library. The `run` method performs the API call based on the provided inputs and returns the status code, headers, and body of the response. If specified in the inputs, it can raise a `ValueError` based on the response status code falling within certain ranges. The `typed.py` file provides type annotations for the inputs and outputs of the `CallAPI` step.