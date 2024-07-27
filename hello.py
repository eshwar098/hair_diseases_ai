from wsgiref.simple_server import make_server
from flask import Flask,redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("house.html")

@app.route("/work")
def work():
    return render_template('work.html')

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)

