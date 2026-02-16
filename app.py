from flask import Flask
from flask import render_template, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")



# Image preprocessing function
def preprocess_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (64, 64))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=-1)

    # Convert image to sequence of 10 frames
    sequence = np.repeat(img[np.newaxis, ...], 10, axis=0)
    sequence = np.expand_dims(sequence, axis=0)
    return sequence

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    file = request.files["image"]
    image = cv2.imdecode(
        np.frombuffer(file.read(), np.uint8),
        cv2.IMREAD_COLOR
    )

    # Step 1: Preprocess image
    input_sequence = preprocess_image(image)

    # Step 2: Show that temporal input is created
    return jsonify({
        "message": "Image uploaded and converted into temporal input successfully",
        "temporal_input_shape": input_sequence.shape,
        "status": "Model architecture integration in progress"
    })

if __name__ == "__main__":
    app.run(debug=True)
