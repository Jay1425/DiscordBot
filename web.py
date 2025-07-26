from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to the Discord Bot Dashboard</h1>"

def run_flask():
    app.run(host="0.0.0.0", port=5000)
