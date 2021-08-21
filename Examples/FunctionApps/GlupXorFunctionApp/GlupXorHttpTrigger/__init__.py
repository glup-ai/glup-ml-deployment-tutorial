import azure.functions as func
from .inference import run

def main(req: func.HttpRequest) -> func.HttpResponse:

    """
    1. Fetch and validate HTTP request.
    """
    x = req.params.get('X')
    y = req.params.get('Y')

    valid_input = ["0", "1"]
    if x not in valid_input or y not in valid_input:
        return func.HttpResponse(f"Pass query X and Y as 0 or 1, f.ex. ?X=0&Y=0",
            status_code=400)

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

    return func.HttpResponse(f"This highly intelligent neural network predicts that {x} XOR {y} = {result}, rounded to {rounded_result}.",
        status_code=200)
