"""
API Endpoint for Touring Machine
"""

from flask import Flask
app = Flask(__name__)

@app.route('/api/v0')
def api():
    return "This is the touring machine api. Please make a post with a origin & destination parameters for output."


if __name__ == '__main__':
    app.run(debug=True)
