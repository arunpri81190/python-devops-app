from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Webhook initialized: Jenkins is ready to build on push!, Assesment completed!!!'

if __name__ == '__main__':
    print('🚀 Flask app starting...')
    print('🔗 GitHub webhook initialized — waiting for push events...')
    print('This is after updating webhook URL and to seen in output')
    app.run(host='0.0.0.0', port=5000)