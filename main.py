from flask import Flask,render_template
henry and mudge
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    