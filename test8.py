from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index8.html')

@app.route('/save', methods=['POST'])
def save_json():
    try:
        json_data = request.form['json']
        # Formatear JSON
        formatted_json = json.dumps(json.loads(json_data), indent=4)
        # Aquí podrías guardar el JSON formateado en una base de datos o en un archivo
        # Por ejemplo:
        # with open('data.json', 'w') as file:
        #     file.write(formatted_json)
        # return 'JSON guardado exitosamente!'
    except Exception as e:
        return f'Error al guardar JSON: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
