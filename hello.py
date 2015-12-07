from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello from Old Trafford!'

@app.route('/health')
def health_check():
    return jsonify({'status':'up'})

service_port=80             # PROD
#service_port=5000          # DEV

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=service_port)