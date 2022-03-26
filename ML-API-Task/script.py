import flask
from flask import Flask, render_template, request

from transform.preprocessing import predict_topic_model, train_topic_model

app = Flask(__name__, template_folder='templates')


@app.route('/init')
def init():
    return flask.render_template('final.html')


@app.route('/train', methods=['POST'])
def train():
    if request.method == 'POST':
        train_topic_model()
        return "Model Trained and Dumped"


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        input_word = request.form['input_word']
        prediction = predict_topic_model(input_word)

        return render_template("result.html", prediction=prediction, input_word= input_word)


if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run(debug=True)
