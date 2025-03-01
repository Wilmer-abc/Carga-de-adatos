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
        print("Columnas encontradas en el Excel:", df.columns.tolist()) 
        
        df.rename(columns={
        'Ventas NA': 'Ventas_NA',
        'Ventas EU': 'Ventas_EU',
        'Ventas JP': 'Ventas_JP',
        'Ventas Otros': 'Ventas_Otros',
        'Ventas Global': 'Ventas_Global'
        }, inplace=True)


        df.fillna({
            'Nombre': 'Desconocido',
            'Plataforma': 'Desconocida',
            'Año': 0,
            'Genero': 'Desconocido',
            'Editorial': 'Desconocido',
            'Ventas_NA': 0,
            'Ventas_EU': 0,
            'Ventas_JP': 0,
            'Ventas_Otros': 0,
            'Ventas_Global': 0
        }, inplace=True)

        data = df.to_dict(orient='records')
        return jsonify({'success': True, 'data': data})

    except Exception as e:
        return jsonify({'error': str(e)})
