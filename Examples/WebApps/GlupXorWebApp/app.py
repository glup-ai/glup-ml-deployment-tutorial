from flask import Flask, request, Response
from inference import run

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def main():

    """
    1. Fetch and validate HTTP request.
    """
    x = request.args.get("X")
    y = request.args.get("Y")

    valid_input = ["0", "1"]
    if x not in valid_input or y not in valid_input:
        return Response(f"Pass query X and Y as 0 or 1, f.ex. ?X=0&Y=0",
        status=400,
        mimetype="text/plain")

    """
    2. Process HTTP request input to valid inference module input.
    """
    input_data = [int(x), int(y)]

    """
    3. Run inference.
    """
    result = run(input_data)

    """
    4. Format API response.
    """
    rounded_result = round(result)

    return Response(f"This highly intelligent neural network predicts that {x} XOR {y} = {result}, rounded to {rounded_result}.",
        status=200,
        mimetype="text/plain")
