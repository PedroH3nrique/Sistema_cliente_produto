from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/adicionarcliente', methods=['GET', 'POST'])
def adicionar_cliente():
    if request.method == 'POST':
        codigo = request.form['codigoClt']
        nome = request.form['nomeClt']
        cidade = request.form['cidadeClt']
        estado = request.form['estadoClt']
        vendedor = request.form['vendedorClt']
        return render_template('relatorios.html', codigo=codigo, nome=nome, cidade=cidade, estado=estado, vendedor=vendedor)
    return render_template('adicionarcliente.html')

@app.route('/relatorios', methods=['GET'])
def relatorios():
    return render_template('relatorios.html')

if __name__ == '__main__':
    app.run(debug=True)