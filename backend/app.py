from flask import Flask, jsonify, request
import json
import os
import requests

app = Flask(__name__)

# A simple health check endpoint
@app.route('/health')
def health():
    return 'OK', 200

# The main data endpoint
@app.route('/api/data')
def get_data():
    s3_json_url = os.environ.get('https://healthy-food-list.s3.ap-southeast-7.amazonaws.com/food.json')

    if s3_json_url:
        try:
            response = requests.get(s3_json_url)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
        except requests.exceptions.RequestException as e:
            return jsonify({'error': str(e)}), 500
    else:
        # Fallback to local file if S3_JSON_URL is not set
        try:
            with open('food.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            return jsonify({'error': 'food.json not found'}), 404

    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
