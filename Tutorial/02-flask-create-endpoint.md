# Creating a Flask Application Endpoint

We start off by setting up a basic Flask application.

## Flask application

**Create a new folder**

```powershell
mkdir GlupWebApp
cd GlupWebApp
```

Create a Python file called *app.py* inside the folder. **NB**: Flask assumes the entry point file to be named *app.py* or *application.py*.

**Create requirements.txt and add Flask to it**
```powershell
echo "Flask==2.0.1" > requirements.txt
```

## Virtual environment

**Create a new virtual environment**
```powershell
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

**Install Flask**
```powershell
(.venv) pip install -r requirements.txt
```

## Add endpoint

**Copy the following contents to app.py**
```python
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def main():
    name = request.args.get("name")
    if not name:
        return Response("Please input your name.", status=400)
    return Response(f"Hello, {name}. This Flask application executed successfully!", status=200)
```

## Run app locally

**Run the app locally to ensure everything works as expected**
```powershell
flask run
```

**The terminal should yield the localhost and port number**
```powershell
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

**Open Postman and run the following** `POST` **query**
```
http://127.0.0.1:5000?name=Aksel
```

**The response should look like this**
```
Hello, Aksel. This Flask application executed successfully!
```

## Next steps

If the response corresponds with the above, proceed to the next step.

[3 - Adding application functionality](03-flask-add-functionality.md)
