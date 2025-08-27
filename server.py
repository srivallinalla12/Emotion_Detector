"""
Flask server for the Emotion Detector application.
Provides an endpoint to analyze text and return detected emotions.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector   # ✅ fixed import

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    API endpoint to detect emotions from a given text query parameter.
    Returns the detected emotions as JSON or an error message if invalid.
    """
    text_to_analyse = request.args.get("text")

    result = emotion_detector(text_to_analyse)

    if result.get("dominant_emotion") is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
