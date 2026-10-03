from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect(url_for('rectangulo_area'))


@app.route('/area', methods=['GET', 'POST'])
def rectangulo_area():
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            base = float(request.form['base'])
            altura = float(request.form['altura'])
            if base <= 0 or altura <= 0:
                error = "La base y la altura deben ser números positivos."
            else:
                resultado = base * altura
        except ValueError:
            error = "Por favor, ingrese valores numéricos válidos."

    return render_template('area.html', resultado=resultado, error=error)


@app.route('/rectangulo_perimetro', methods=['GET', 'POST'])
def rectangulo_perimetro():
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            base = float(request.form['base'])
            altura = float(request.form['altura'])
            if base <= 0 or altura <= 0:
                error = "La base y la altura deben ser números positivos."
            else:

                resultado = 2 * (base + altura)
        except ValueError:
            error = "Por favor, ingrese valores numéricos válidos."

    return render_template('rectangulo_perimetro.html', resultado=resultado, error=error)

if __name__ == '__main__':
    app.run(debug=True)
