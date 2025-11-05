from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from your Python DevOps App!"

@app.route('/metrics')
def metrics():
    return "app_requests_total 42\napp_errors_total 3"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)