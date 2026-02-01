from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    score = None
    limite = None
    idade = None

    if request.method == 'POST':
        idade = request.form.get('idade')
        renda = request.form.get('renda')
        divida = request.form.get('divida')

        idade = request.form.get("idade")

        if not idade or int(idade) < 18:
            return render_template("index.html", erro="Idade inválida")

        if renda and divida:
            if divida == 'sim':
                score = random.randint(0, 600)
            else:
                score = random.randint(600, 1000)

            if score <= 250:
                limite = 500
            elif score <= 400:
                limite = 1000
            elif score <= 650:
                limite = 2500
            elif score <= 899:
                limite = 5000
            else:
                limite = 10000

    return render_template('index.html', score=score, limite=limite, idade=idade)

if __name__ == '__main__':
    app.run(debug=True)

    

