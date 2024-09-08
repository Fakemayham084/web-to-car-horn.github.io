from flask import Flask, render_template, request
import requests

app = Flask(__name__)

ESP32_IP = "http://10.0.0.90"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blink', methods=['POST'])
def blink_led():
    try:
        response = requests.get(f'{ESP32_IP}/blink')
        if response.status_code == 200:
            return "LED Blinking"
        else:
            return "Failed to send request", 500
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
