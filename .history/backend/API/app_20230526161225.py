from flask import Flask 

app = Flask(__name__)

import main 

@app.route("/")
def home():
    return "Bem-vindo ao website da rede!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)