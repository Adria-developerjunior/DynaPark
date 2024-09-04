from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        cpf = request.form['cpf']
        phone = request.form['phone']
        ra = request.form['ra']
        drt = request.form['drt']
        employee_code = request.form['employee_code']
        # Aqui você deve adicionar lógica para salvar os dados do usuário
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/register-vehicle', methods=['POST'])
def register_vehicle():
    vehicle_plate = request.form['vehicle_plate']
    vehicle_model = request.form['vehicle_model']
    vehicle_color = request.form['vehicle_color']
    # Aqui você deve adicionar lógica para salvar os dados do veículo
    return redirect(url_for('index'))

@app.route('/process-payment', methods=['POST'])
def process_payment():
    payment_method = request.form['payment_method']
    amount = request.form['amount']
    duration = request.form['duration']
    # Aqui você deve adicionar lógica para processar o pagamento
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
