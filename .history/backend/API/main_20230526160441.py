from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
    return "Bem-vindo ao website da rede!"

if __name__ == '__main__':
    app.run(host="0.0.0.0.", port=8000, debug=True)