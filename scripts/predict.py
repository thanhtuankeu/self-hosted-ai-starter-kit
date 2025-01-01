from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the model
# model = tf.keras.models.load_model('model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # Parse JSON input
    input_data = request.json.get("data", [])
    input_array = np.array(input_data).reshape(1, -1)
    # predictions = model.predict(input_array)
    predictions = {"predictions": [0, 1, 2, 3, 4]}
    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
