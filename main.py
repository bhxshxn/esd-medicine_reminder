from flask import Flask, render_template, url_for, request
from twilio.rest import Client


app = Flask(__name__, static_folder='static', template_folder="template")


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/form")
def form():
    return render_template('form.html')


@app.route('/save', methods=['POST', 'GET'])
def save():
    time = request.form['time']
    text = request.form['text']
    num = request.form['number']
    data = [time, text, num]
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
