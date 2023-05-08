from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def stress_cpu():

    if request.method == 'POST':
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return jsonify(sucess=True)
    else:
        return socket.gethostname()


if __name__ == '__main__':
    app.run()
