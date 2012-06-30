"""
API Endpoint for Touring Machine
"""

import requests

from flask import Flask, request
app = Flask(__name__)


@app.route('/api/v0', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        if request.form['origin'] and request.form['destination']:
            params = {
                'origin': request.form['origin'],
                'destination': request.form['destination'],
                'sensor': 'false'
            }
            gmaps_api = 'http://maps.googleapis.com/maps/api/directions/json'
            r = requests.get(gmaps_api, params=params)
            return r.text
    else:
        return "This is the touring machine api.\
            Please POST with origin & destination parameters for valid output."


if __name__ == '__main__':
    app.run(debug=True)
