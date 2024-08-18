from flask import Flask, render_template
from flask import jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/streamlit")
def streamlit_embed():
    output = subprocess.run(
        ['streamlit', 'run', 'app.py', '--server.port', '8501'],
        capture_output=True,
        text=True
    )

    return output.stdout

if __name__ == "__main__":
    app.run(debug=True)
