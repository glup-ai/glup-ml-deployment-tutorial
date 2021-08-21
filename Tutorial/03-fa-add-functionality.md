# Adding Application Functionality

We need to add application functionality to the HTTP trigger endpoint.

## Import inference module

Copy `inference.py` and the trained models to folder `/GlupHttpTrigger`.

Import the inference execution method to `__init__.py`.

```python
import logging
import azure.functions as func
from .inference import run

def main(req: func.HttpRequest) -> func.HttpResponse:
    ...
```

All necessary files and sub folders should now be present in the [/GlupFunctionApp](../Examples/FunctionApps/GlupFunctionApp) folder (additional files may also be present).

```
GlupFunctionApp/
| - .venv/
| - GlupHttpTrigger/
| | - __init__.py
| | - inference.py
| | - function.json
| | - trained_models/
| | | - lmks_model/
| | | - model/
| - .funcignore
| - host.json
| - local.settings.json
| - requirements.txt
```

## Install requirements

Install all necessary Python packages within the virtual environment. Make sure to include all packages and versions that are imported in `inference.py`, as well as the [Azure Functions Python library](https://pypi.org/project/azure-functions/) (`requirements.txt` includes `azure-functions` by default).

Our implementation consists of [the following dependencies](../Examples/FunctionApps/GlupFunctionApp/requirements.txt).

```powershell
(.venv) pip install -r requirements.txt
```

## Change init.py

The HTTP-triggered function endpoint must contain the following functionality:
1. Fetch and validate HTTP request.
2. Process HTTP request input to valid inference module input.
3. Run inference.
4. Format API response.

**Step 3.** is already managed by importing the `inference.py` module. **Steps 1., 2.,** and **4.** vary based on the model input and output.

For our application, the steps are carried out [like this](../Examples/FunctionApps/GlupFunctionApp/GlupHttpTrigger/__init__.py). The XOR application `__init__.py` module looks [like this](../Examples/FunctionApps/GlupXorFunctionApp/GlupXorHttpTrigger/__init__.py).

## Run function locally

Run the function app locally to ensure everything works as expected. Download an image of a cat and a set of .PNG formatted shades or fetch a couple of shades [from here](images/shades).

[Click here](./postman-request-with-images.md) for a description of how to use Postman to process HTTP requests with images.

![Response](images/cat_03.jpg)

## Next steps

If Postman displays the predicted result, we are ready to deploy the function app to Azure.

[4 - Deploying the Function app to Azure](04-fa-deploy-to-azure.md)
