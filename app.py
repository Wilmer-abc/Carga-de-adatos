from flask import Flask, render_template
from rutas.cargar import cargar_archivo
from rutas.guardar import guardar_bd

app = Flask(__name__)

# Registrar rutas
app.register_blueprint(cargar_archivo)
app.register_blueprint(guardar_bd)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
