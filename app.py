from flask import Flask, request

app = Flask(__name__)

@app.route('/bgmi', methods=['GET'])
def bgmi():
    ip = request.args.get('ip')
    port = request.args.get('port')
    time = request.args.get('time')
    return f"Received IP: {ip}, Port: {port}, Time: {time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
