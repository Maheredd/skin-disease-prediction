from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import os

# Disable OneDNN optimizations (optional fix for CPU bugs on some systems)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = load_model("skin_disease_model.h5")


# Define class labels
class_names = [
    "Cellulitis", "Impetigo", "Athelete-Foot", "Nail-Fungus",
    "Ringworm", "Cutaneous-larva-migrans", "Chickenpox", "Shingles"
]

# Preprocess input image
def preprocess_image(img, target_size=(150, 150)):
    img = img.convert("RGB")  # Ensure it's 3-channel
    img = img.resize(target_size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize
    return img_array

# Main route
@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        file = request.files.get("file")
        if file:
            image = Image.open(file.stream)
            processed = preprocess_image(image)
            preds = model.predict(processed)
            predicted_class = class_names[np.argmax(preds)]
            prediction = predicted_class

    return render_template("index.html", prediction=prediction)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
