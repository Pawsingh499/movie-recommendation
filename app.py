from flask import Flask, jsonify, render_template, request
from werkzeug.wrappers import response
from model import make_recommendation

# webapp
app = Flask(__name__, template_folder='templates')


@app.route('/')
def main():
    return render_template('index.html')


@app.route("/")
def get_recommendations():
    genres = request.form.get('genres')
    actor = request.form.get('actor')
    director = request.form.get('director')
    userText = genres + " " + actor+" "+ director
    response = make_recommendation(str(userText))
    return jsonify(response)
    
    


if __name__ == '__main__':
    app.run(debug=True)
