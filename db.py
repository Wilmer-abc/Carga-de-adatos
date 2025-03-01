import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Qwerty123",
    database="PrimerParcial2",
    port=3307 
)
