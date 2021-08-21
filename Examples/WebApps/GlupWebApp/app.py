from PIL import Image
from six import BytesIO
from flask import Flask, request, Response
from inference import run

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def main():
    """
    1. Fetch and validate HTTP request.
    """
    input_files = request.files
    if (len(input_files) != 2):
        return Response("Invalid input.", status=400, mimetype="text/plain")

    glasses = input_files.get("glasses", "")
    cat = input_files.get("cat", "")
    
    """
    2. Process HTTP request input to valid inference module input.
    """
    image_glasses = open_image(glasses)
    image_cat = open_image(cat)
    
    """
    3. Run inference.
    """
    image_result = run(image_glasses, image_cat)

    """
    4. Format API response.
    """
    api_response = process_api_response(image_result)
    
    return api_response

def open_image(input_file):
    return Image.open(input_file)

def process_api_response(image_inference):
    result_image = Image.fromarray(image_inference)
    image_byte_array = BytesIO()
    result_image.save(image_byte_array, format="JPEG")
    api_response = image_byte_array.getvalue()

    return Response(api_response, status=200, mimetype="image/jpeg")
