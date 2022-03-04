from sentiment_classifier import SentimentClassifier
import time
from flask import Flask, render_template, request

app = Flask(__name__)

print("Preparing classifier")
start_time = time.time()
classifier = SentimentClassifier()
print("Classifier is ready")
print(time.time() - start_time, "seconds")


@app.route("/")
def hello():
    return "Add '/sentiment-demo' to web path"


@app.route("/sentiment-demo", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
        prediction_message = classifier.predict_text(text)

    return render_template('template.html', text=text, prediction_message=prediction_message)


if __name__ == "__main__":
    app.run(debug=True)
