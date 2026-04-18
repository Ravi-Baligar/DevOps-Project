from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("APP_ENV", "unknown")
    message = os.getenv("APP_MESSAGE", "Default message")
    return f"""
    <h2>DevOps Assignment Successful </h2>
    <p>Environment: {env}</p>
    <p>Message: {message}</p>
    """

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)