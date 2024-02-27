from flask import Flask, request, render_template

app = Flask(__name__)

# Ruta para renderizar el formulario
@app.route('/')
def index():
    modelos = ["Python 2", "Python 3"]
    return render_template('index.html', modelos=modelos)

# Ruta para manejar la solicitud POST
@app.route('/ruta_de_tu_flask', methods=['POST'])
def recibir_valor_seleccionado():
    selected_python = request.form['selectedPython']
    # Aquí puedes hacer lo que necesites con el valor seleccionado
    print("Valor seleccionado:", selected_python)
    return 'Valor seleccionado recibido: ' + selected_python

if __name__ == '__main__':
    app.run(debug=True)
