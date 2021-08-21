# Adding Application Functionality

We need to add application functionality to the Flask endpoint.

## Import inference module

Copy `inference.py` and the trained models to folder `/GlupWebApp`.

Import the inference execution method to `app.py`.

```python
from flask import Flask, request, Response
from inference import run

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def main():
    ...
```

All necessary files and sub folders should now be present in the [/GlupWebApp](../Examples/WebApps/GlupWebApp) folder (additional files may also be present).

```
GlupWebApp/
| - .venv/
| - app.py
| - inference.py
| - trained_models/
| | - lmks_model/
| | - model/
| - requirements.txt
```

## Install requirements

Install all necessary Python packages within the virtual environment. Make sure to include all packages and versions that are imported in `inference.py`, as well as the already included Flask module.

Our implementation consists of [the following dependencies](../Examples/WebApps/GlupWebApp/requirements.txt).

```powershell
(.venv) pip install -r requirements.txt
```

## Change app.py

The HTTP-triggered Flask endpoint must contain the following functionality:
1. Fetch and validate HTTP request.
2. Process HTTP request input to valid inference module input.
3. Run inference.
4. Format API response.

**Step 3.** is already managed by importing the `inference.py` module. **Steps 1., 2.,** and **4.** vary based on the model input and output.

For our application, the steps are carried out [like this](../Examples/WebApps/GlupWebApp/app.py). The XOR application `app.py` module looks [like this](../Examples/WebApps/GlupXorWebApp/app.py).

## Run application locally

Run the application locally to ensure everything works as expected. Download an image of a cat and a set of .PNG formatted shades or fetch a couple of shades [from here](images/shades).

[Click here](./postman-request-with-images.md) for a description of how to use Postman to process HTTP requests with images.

![Response](images/cat_04.jpg)

## Next steps

If Postman displays the predicted result, we are ready to deploy the Flask application to Azure.

[4 - Deploying the Flask application to Azure](04-flask-deploy-to-azure.md)
