from flask import Blueprint, request, jsonify
from db import conectar_bd

guardar_bd = Blueprint('guardar_bd', __name__)

@guardar_bd.route('/guardar', methods=['POST'])
def guardar():
    try:
        datos = request.json['data']
        conexion = conectar_bd()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO VideoJuego1 (
                Nombre, Plataforma, Año, Genero, Editorial, 
                Ventas_NA, Ventas_EU, Ventas_JP, Ventas_Otros, Ventas_Global
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for row in datos:
            valores = (
                row['Nombre'], row['Plataforma'], row['Año'], row['Genero'], row['Editorial'], 
                row['Ventas_NA'], row['Ventas_EU'], row['Ventas_JP'], row['Ventas_Otros'], row['Ventas_Global']
            )
            cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        return jsonify({'success': True, 'message': 'Datos guardados correctamente en la BD'})

    except Exception as e:
        return jsonify({'error': str(e)})
