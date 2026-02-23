from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Hello from the Python Back-End!</h1><p>Live Server Time: {current_time}</p>"

if __name__ == '__main__':
    # Running on port 5000 (Internal Only)
    app.run(host='0.0.0.0', port=5000)
