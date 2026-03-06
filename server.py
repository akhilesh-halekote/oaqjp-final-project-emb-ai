from Flask import flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('\emotionDetector')
def emotion_analysis():
    text = request.form['textToAnalyze']
    res = emotion_detector(text)