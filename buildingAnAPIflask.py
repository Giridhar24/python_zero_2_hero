# Topic of the Day: Building an API (Flask)
# Explanation: So far, our Python code only runs on our machine.
# Flask is a micro-framework that turns your Python code into a Web Server.
# It listens for requests (like a browser visiting a URL) and returns data.
# @app.route: Maps a URL (like /hello) to a function.

from flask import Flask, jsonify

app = Flask(__name__)

# 1. Define a Route
# When a user visits 'http://localhost:5000/', run this:
@app.route('/')
def home():
    return "Welcome to my Python API!"

# 2. Return JSON Data
# When a user visits 'http://localhost:5000/api/data', run this:
@app.route('/api/data')
def get_data():
    sample_data = {
        "id": 1,
        "name": "Hero User",
        "status": "Active"
    }
    return jsonify(sample_data)

# 3. Run the Server
if __name__ == '__main__':
    app.run(debug=True)