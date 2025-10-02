from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap4
app = Flask(__name__)
bootstrap = Bootstrap4(app)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/blog.html")
def blog():
    return render_template('blog.html')

@app.route("/contact.html")
def contacto():
    return render_template('contact.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/matches.html")
def juegos():
    return render_template('matches.html')

@app.route("/players.html")
def jugadores():
    return render_template('players.html')

@app.route("/single.html")
def single():
    return render_template('single.html')



if __name__ == "__main__":
    app.run(debug=True)