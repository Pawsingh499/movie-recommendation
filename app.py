from flask import Flask, jsonify, render_template, request
from model import make_recommendation

# webapp
app = Flask(__name__, template_folder='./')


@app.route('/')
def main():
    return render_template('index.html')


@app.route("/get")
def get_recommendations():
    userText = request.args.get('msg')
    response = make_recommendation(str(userText))
    return jsonify(response)
