from tensorflow.keras.models import load_model
from numpy import array

def run(input_data):

    """
    1. Load trained model.
    """
    model = load_model("model")

    """
    2. Process inference input to valid model format.
    """
    X = array([input_data])

    """
    3. Run model.
    """
    predicted_value = model.predict(X)

    """
    4. Process and return inference results.
    """
    return predicted_value[0][0]
