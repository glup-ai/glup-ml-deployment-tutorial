# Creating an Azure Function App Endpoint

We start off by creating an Azure function app using **Azure Functions Core tools**.

## Azure function app

**Create a new Python function app**
```powershell
func init GlupFunctionApp --worker-runtime python
```

## Virtual environment

**Create a new virtual environment inside the function app folder**
```powershell
cd GlupFunctionApp
python -m venv .venv
```

**Activate the environment**

Windows
```powershell
.venv/Scripts/activate
```
Mac / Linux
```
source .venv/bin/activate
```

## Azure function

**Create a new HTTP-triggered Azure function template**
```powershell
func new --name GlupHttpTrigger --template "HTTP trigger"
```

**Make a couple of adjustments in function.json**
- Change `authLevel` from `function` to `anonymous` so that [no API key is required](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=csharp#configuration). 
- Remove `get` from `methods`, as we only need `post`.
```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "authLevel": "anonymous",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": [
        "post"
      ]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    }
  ]
}
```

## Run function locally

**Run the function app locally to ensure everything works as expected**
```powershell
func start
```

**The terminal should yield the localhost and port number**
```powershell
GlupHttpTrigger: [POST] http://localhost:7071/api/GlupHttpTrigger
```

**Open Postman and run the following** `POST` **query**
```powershell
http://localhost:7071/api/GlupHttpTrigger?name=Aksel
```

**The response should look like this**
```
Hello, Aksel. This HTTP triggered function executed successfully.
```

## Next steps

If the response corresponds with the above, proceed to the next step.

[3 - Adding application functionality](03-fa-add-functionality.md)
