from flask import Flask
app = Flask(__name__)

@app.route('/health_check')
def health_check():
    return 'all good'
