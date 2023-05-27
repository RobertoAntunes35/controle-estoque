from flask import Flask, render_template


import main as m 

m.crudCliente
m.crudFornecedor
m.crudProduto
m.crudVendedores


app = Flask(__name__)

@app.route("/teste")
def index():
    valueTeste = m.produtos.filter_by(codigo = 254).first()
    return render_template('index.html')
 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)