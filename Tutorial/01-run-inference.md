# Running Inference on a Trained ML Model

Initially, we need to acquire an ML model. Using TensorFlow/Keras, we must [save and serialize](https://www.tensorflow.org/guide/keras/save_and_serialize) our trained model.  

This tutorial will adopt a model based on the [Cat Hipsterizer repository](https://github.com/kairess/cat_hipsterizer). We have already run the code and obtained the [trained models](../Examples/FunctionApps/GlupFunctionApp/GlupHttpTrigger/trained_models). These can be copied, but feel free to train and use your own models instead.

## Inference module

Further, we need an inference module `inference.py` with an execution method `run(*input_data)` which
1. Loads the trained model(s).
2. Processes the inference input data to a valid model input format.
3. Run the model(s) with the processed data.
4. Processes and returns the inference results.

The listed functionality is required to be able to run the ML algorithm with new input data.

The provided example [inference module](../Examples/FunctionApps/GlupFunctionApp/GlupHttpTrigger/inference.py) includes image processing and multiple models, yielding a somewhat complex data processing. In many cases, particularly applications without image processing such as an [XOR application](../Examples/FunctionApps/GlupXorFunctionApp/GlupXorHttpTrigger/inference.py), the steps are substantially less intricate.

## Next steps

When the inference module is established, proceed to the next step.

The subsequent stages varies based on the desired service architecture. If you intend to follow the provided tutorial example, or your inference module consists of the [OpenCV module](https://pypi.org/project/opencv-python/) dependency, we recommend to choose the serverless function app configuration. Python Azure app service on Linux does not yet contain off the shelf OpenCV support. Otherwise, the Flask app service approach is a good starting point.

[2 - Creating an Azure Function app endpoint](02-fa-create-endpoint.md)

or

[2 - Creating a Flask application endpoint](02-flask-create-endpoint.md)
