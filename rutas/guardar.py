from flask import Blueprint, request, jsonify
from db import conectar_bd

guardar_bd = Blueprint('guardar_bd', __name__)

@guardar_bd.route('/guardar', methods=['POST'])
def guardar():
    try:
        datos = request.json
        paises = datos.get('paises', [])
        poblacion = datos.get('poblacion', [])

        if not paises and not poblacion:
            return jsonify({'error': 'No se recibieron datos'}), 400

        conexion = conectar_bd()
        cursor = conexion.cursor()

        # Guardar datos en la tabla Countries
        if paises:
            sql_paises = """
                INSERT INTO Countries (Country_Code, Country, Continent)
                VALUES (%s, %s, %s)
            """
            for row in paises:
                valores = (row.get('Country_Code', 'Desconocido'),
                           row.get('Country', 'Desconocida'),
                           row.get('Continent', 'Desconocida'))
                cursor.execute(sql_paises, valores)

        # Guardar datos en la tabla Population
        if poblacion:
            sql_poblacion = """
                INSERT INTO Population (Country, Population)
                VALUES (%s, %s)
            """
            for row in poblacion:
                valores = (row.get('Country', 'Desconocida'),
                           row.get('Population', '0'))
                cursor.execute(sql_poblacion, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        return jsonify({'success': True, 'message': 'Datos guardados correctamente en la BD'})

    except Exception as e:
        return jsonify({'error': str(e)})
