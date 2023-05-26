from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
    return "Bem-vindo ao website da rede!"

if __name__ == '__main__':
    app.run(debug=True)