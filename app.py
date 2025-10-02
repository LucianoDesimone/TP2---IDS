from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap4
app = Flask(__name__)
bootstrap = Bootstrap4(app)

@app.route("/")
@app.route("/registration.html")
def registration():
    return render_template('registration.html')

@app.route("/index.html")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port = 8000)