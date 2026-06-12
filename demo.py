import numpy as np
import gradio as gr

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image

# Load model
model = load_model("best_model.h5")

# Class names
CLASS_NAMES = [
    'cataract',
    'diabetic_retinopathy',
    'glaucoma',
    'normal'
]

# Prediction function
def predict_disease(img):

    # Resize image
    img_resized = img.resize((224, 224))

    # Convert image to array
    img_array = keras_image.img_to_array(img_resized) / 255.0

    # Expand dimensions
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)[0]

    # Convert to readable output
    result = {
        CLASS_NAMES[i]: float(predictions[i])
        for i in range(len(CLASS_NAMES))
    }

    return result

# Gradio Interface
demo = gr.Interface(
    fn=predict_disease,

    inputs=gr.Image(
        type="pil",
        label="Upload Retinal Image"
    ),

    outputs=gr.Label(
        num_top_classes=4,
        label="Prediction"
    ),

    title="Eye Disease Detection System",

    description="""
    Upload a retinal image to detect:
    - Cataract
    - Diabetic Retinopathy
    - Glaucoma
    - Normal
    """
)

# Launch app
demo.launch()