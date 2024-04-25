# CreatePRComment class in CreatePRComment.py

The `CreatePRComment` class is used to set up and manage the creation of pull request comments.

## `__init__` Method
The `__init__` method initializes the `CreatePRComment` class with a dictionary of inputs. 

### Inputs
This method expects the following keys in the `inputs` dictionary:

- "pr_url" : URL of the pull request
- "pr_comments" : Comments to be added to the pull request
- "github_api_key" or "gitlab_api_key" : API key for Github or Gitlab. One of these keys is necessary for the method to run
- "scm_url" : (Optional) source control manager URL
- "noisy_comments": (Optional) Boolean that defaults to False. If set to True, comments will not be reset
  
The method sets up either a `GithubClient` or `GitlabClient` instance depending on the provided API key. It also handles setting the source control manager URL if provided and extracts the pull request and comments from the inputs.

### Output
This method does not return an output. It mostly sets up the class variables for usage in other methods.

## `run` Method
The `run` method handles the actual creation of comments.

### Inputs
The `run` method does not expect any explicit inputs because it uses the values initialized during the object instantiation.

### Output
The `run` method creates comments on the specified pull request URL stored in the class instance. It first checks if 'noisy_comments' is set to False (default) and resets all the existing comments. Then, it loops through each comment in 'pr_comments' and creates them on the pull request. 

The method does not explicitly return any values, but after successful execution will have created the specified comments on the pull request associated with the object instance. The 'run' method returns an empty dictionary after successful completion of comment creation.
