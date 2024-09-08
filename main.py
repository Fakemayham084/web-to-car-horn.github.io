from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ESP_URL = 'http://10.0.0.90/blink'

@app.route('/trigger', methods=['POST'])
def trigger_esp():
    try:
        response = requests.get(ESP_URL)
        response.raise_for_status()  
        return jsonify({"message": "Request sent to ESP", "esp_response": response.text}), 200
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error sending request to ESP: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
