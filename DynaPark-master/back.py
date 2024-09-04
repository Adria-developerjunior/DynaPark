import sqlite3
from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__, template_folder= 'teste', static_folder='teste/index.html')

def init_db():
    #cria o banco de dados na pasta DynaPark
    try: 
        conn = sqlite3.connect('user_data.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users (
            ID INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
            name STRING(100) NOT NULL,
            cpf STRING(14) NOT NULL UNIQUE,
            phone STRING(20) NOT NULL,
            ra STRING(20) NOT NULL UNIQUE,
            drt STRING(20),
            employee_code STRING(20) NOT NULL UNIQUE
            )
            ''')
        conn.commit()
        conn.close()
        print('Banco de Dados criado com sucesso')
    except Exception as e:
        print(f"Erro em inicializar Banco de Dados")
        
init_db()

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_user():
    try:
        name = request.form['name']
        cpf = request.form['cpf']
        phone = request.form['phone']
        ra = request.form['ra']
        drt = request.form['drt']
        employee_code = request.form['employee_code']
        # Aqui você deve adicionar lógica para salvar os dados do usuário
        print(f"Recebido dados: Nome={name}, CPF={cpf}, Phone={phone}, RA={ra}, DRT={drt},employee_code={employee_code}")
        #Recebe os dados e bota eles no banco de dados
        conn = sqlite3.connect('user_data.db')
        cur = conn.cursor()
        #Insere os dados no banco de dados
        cur.execute('''INSERT INTO users(name, cpf, phone, ra, drt, employee_code)
                    VALUES (?,?,?,?,?,?)''',(name, cpf, phone, ra, drt, employee_code))
        
        conn.commit()
        conn.close()
        
        print(f"Usuario {name} registrado")
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Erro em registrar: {e}")
        return "Um erro ocorreu durante a registraçao"
    
@app.route('/login')
def login():
    return render_template('login.html')
#forma de login
@app.route('/login', methods=['POST'])
def login():
    try:
        #recebe os dados nome e cpf
        name = request.form['name']
        cpf = request.form['cpf']
        
        print(f"Recebido dados nome={name}, cpf={cpf}")
        
        conn = sqlite3.connect('user_data.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE name = ? AND cpf = ?',(name, cpf))
        user = cur.fetchone()
        conn.close()
        
        if user:
            print(f"login realizado com sucesso para usuario: {name[1]}")
            return redirect(url_for('index'))
        else:
            print("Login failed. Incorrect email or password.")
            flash('Incorrect email or password. Please try again.')
            return redirect(url_for('show_login'))
    except Exception as e:
        print(f"Error during login: {str(e)}")
        flash('An error occurred during login. Please try again.')
        return redirect(url_for('show_login'))
        
    
        

#@app.route('/register-vehicle', methods=['POST'])
#def register_vehicle():
   # vehicle_plate = request.form['vehicle_plate']
   # vehicle_model = request.form['vehicle_model']
   # vehicle_color = request.form['vehicle_color']
    # Aqui você deve adicionar lógica para salvar os dados do veículo
   # return redirect(url_for('index'))

#@app.route('/process-payment', methods=['POST'])
#def process_payment():
    #payment_method = request.form['payment_method']
    #amount = request.form['amount']
    #duration = request.form['duration']
    # Aqui você deve adicionar lógica para processar o pagamento
   # return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
