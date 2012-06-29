"""
API Endpoint for Touring Machine
"""

from flask import Flask, request
app = Flask(__name__)


@app.route('/api/v0', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        return "{'DUMMY': 'DATA'}"
    else:
        return "This is the touring machine api.\
            Please POST with origin & destination parameters for valid output."


if __name__ == '__main__':
    app.run(debug=True)
