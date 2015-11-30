from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello from Reading, PA!'

@app.route('/health')
def health_check():
    return jsonify({'status':'up'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')