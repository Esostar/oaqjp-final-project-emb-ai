import requests
import json


def emotion_detector(text_to_analyze):
    """
    Analyze text using Watson NLP EmotionPredict API
    and return the formatted emotion scores with the dominant emotion.
    """

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send request to Watson API
    response = requests.post(url, headers=headers, json=payload)

    # Convert response text to dictionary
    response_dict = json.loads(response.text)

    # Extract emotion scores
    emotions = response_dict['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return formatted output
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }