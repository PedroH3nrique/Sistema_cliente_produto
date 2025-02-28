from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            codigo INTEGER PRIMARY KEY,  -- Código como chave primária
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            vendedor TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_cliente(codigo, nome, cidade, estado, vendedor):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO clientes (codigo, nome, cidade, estado, vendedor)
            VALUES (?, ?, ?, ?, ?)
        ''', (codigo, nome, cidade, estado, vendedor))
        conn.commit()
    except sqlite3.IntegrityError:
        # Se o código já existir, lança uma exceção
        raise ValueError("Código já existe.")
    finally:
        conn.close()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/adicionarcliente', methods=['GET', 'POST'])
def adicionar_cliente():
    if request.method == 'POST':
        try:
            codigo = int(request.form['codigoClt'])  # Tenta converter para inteiro
            nome = request.form['nomeClt']
            cidade = request.form['cidadeClt']
            estado = request.form['estadoClt']
            vendedor = request.form['vendedorClt']
            
            # Adiciona o cliente ao banco de dados
            add_cliente(codigo, nome, cidade, estado, vendedor)
            
            return redirect(url_for('relatorios'))
        except ValueError as e:
            # Se a conversão falhar ou o código já existir
            return render_template('adicionarcliente.html', error=str(e))
    
    return render_template('adicionarcliente.html')

@app.route('/relatorios', methods=['GET'])
def relatorios():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conn.close()
    
    return render_template('relatorios.html', clientes=clientes)

if __name__ == '__main__':
    init_db()  # Inicializa o banco de dados
    app.run(debug=True)