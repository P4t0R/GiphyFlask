from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/ruta_de_tu_flask', methods=['POST'])
def recibir_datos():
    dni = request.form['dni']
    tipo = request.form['tipo']
    ambiente = request.form['ambiente']

    # Aquí puedes hacer lo que necesites con los datos recibidos
    print(f"DNI: {dni}, Tipo: {tipo}, Ambiente: {ambiente}")

    return 'Datos recibidos correctamente'

if __name__ == '__main__':
    app.run(debug=True)
