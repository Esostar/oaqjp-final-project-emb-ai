# server.py
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector  # import your packaged function

# Initialize Flask app
app = Flask(__name__)

# Route for homepage
@app.route("/")
def render_index_page():
    return render_template("index.html")

# Route for emotion detection
@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')

    # Call your emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Handle blank or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response

# Run the Flask app on port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)