"""
API Endpoint for Touring Machine
"""

from flask import Flask
app = Flask(__name__)

@app.route('/api/v0')
def api():
    return "Hello, API World!"


if __name__ == '__main__':
    app.run(debug=True)
