from Flask import flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_analysis():
    text = request.form['textToAnalyze']
    res = emotion_detector(text)
    request.form['system_response'] = r the given statement, the system response is 'anger'': {res['anger']}, 'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': {res['sadness']}. The dominant emotion is {res['dominant_emotion']}."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)