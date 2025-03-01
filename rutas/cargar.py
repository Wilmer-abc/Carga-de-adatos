from flask import Blueprint, request, jsonify
import pandas as pd

cargar_archivo = Blueprint('cargar_archivo', __name__)

@cargar_archivo.route('/cargar', methods=['POST'])
def cargar():
    if 'archivo' not in request.files:
        return jsonify({'error': 'No se envió ningún archivo'})

    archivo = request.files['archivo']
    if archivo.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'})

    try:
        df = pd.read_excel(archivo)
        columnas = df.columns.tolist()
        print("Columnas encontradas:", columnas)

        if 'Country Code' in columnas and 'Continent' in columnas:
            df.rename(columns={'Country Code': 'Country_Code'}, inplace=True)
            df.fillna({'Country_Code': 'Desconocido', 'Country': 'Desconocida', 'Continent': 'Desconocida'}, inplace=True)
            data = df.to_dict(orient='records')
            return jsonify({'success': True, 'tipo': 'paises', 'data': data})

        elif 'Country' in columnas and 'Population' in columnas:
            df.fillna({'Country': 'Desconocida', 'Population': 'Desconocida'}, inplace=True)
            data = df.to_dict(orient='records')
            return jsonify({'success': True, 'tipo': 'poblacion', 'data': data})

        else:
            return jsonify({'error': 'Formato de archivo no reconocido'})

    except Exception as e:
        return jsonify({'error': str(e)})
