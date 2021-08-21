import azure.functions as func
from PIL import Image
from six import BytesIO
from .inference import run


def main(req: func.HttpRequest) -> func.HttpResponse:

    """
    1. Fetch and validate HTTP request.
    """
    input_files = list(req.files.values())

    if (len(input_files) != 2):
        return func.HttpResponse("Invalid input", status_code=400)

    glasses = input_files[0]
    cat = input_files[1]
    
    """
    2. Process HTTP request input to valid inference module input.
    """
    image_glasses = convert_stream_to_image(glasses)
    image_cat = convert_stream_to_image(cat)
    
    """
    3. Run inference.
    """
    image_result = run(image_glasses, image_cat)

    """
    4. Format API response.
    """
    api_response = process_api_response(image_result, func)
    
    return func.HttpResponse(api_response, status_code=200)

def convert_stream_to_image(input_file):
    contents = input_file.stream.read()
    image_byte_array = BytesIO(contents)
    image = Image.open(image_byte_array)

    return image

def process_api_response(image_inference, func):
    func.HttpResponse.mimetype = 'image/jpeg'

    result_image = Image.fromarray(image_inference)
    image_byte_array = BytesIO()
    result_image.save(image_byte_array, format='JPEG')
    api_response = image_byte_array.getvalue()

    return api_response
