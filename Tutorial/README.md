# Machine Learning API Deployment Tutorial

In the following tutorial, we are going to deploy a trained TensorFlow/Keras machine learning application to the Azure cloud infrastructure as a RESTful API. The procedure consists of two distinct approaches. Choose the service architecture that best suits your ML application.

We will present deployment solutions based on the following Azure services:
- [Serverless function app](https://docs.microsoft.com/en-us/azure/azure-functions/)
- [Hosted app service](https://docs.microsoft.com/en-us/azure/app-service/), using the [Flask framework](https://flask.palletsprojects.com/en/2.0.x/quickstart/)

## Prerequisites

- **Azure account**: Use your existing account or sign up [here](https://azure.microsoft.com/en-us/free/).
- **Azure CLI**: For deployment to Azure. Install [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
- **Azure Functions Core tools v3**: For serverless function app local development. Install [here](https://github.com/Azure/azure-functions-core-tools).
- **Python**: TensorFlow/Keras programming language. Azure functions v3 and Azure app service supports Python 3.6, 3.7 and 3.8. We will use Python 3.8 in our examples. Download [here](https://www.python.org/downloads/).
- **Virtualenv**: Isolated Python environment for local development. Install [here](https://virtualenv.pypa.io/en/latest/installation.html).
- **Postman**: For testing purposes. Download [here](https://www.postman.com/downloads/).

**Ensure everything is installed**

Azure Functions Core tools. Must be v3.
```powershell
PS C:\> func --version
3.0.3568
```

Azure CLI verison may differ.
```powershell
PS C:\> az --version
azure-cli                         2.26.0 *

core                              2.26.0 *
telemetry                          1.0.6
```

```powershell
PS C:\> python --version
Python 3.8.3
```

## Next steps

If everything is installed, proceed to the next step.

[1 - Running inference on a trained ML model](01-run-inference.md)
