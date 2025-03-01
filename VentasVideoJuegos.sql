Create database VentasVideoJuegos;
use VentasVideoJuegos;

CREATE TABLE VideoJuego1 (
    Nombre VARCHAR(255),
    Plataforma VARCHAR(100),
    Año INT,
    Genero VARCHAR(100),
    Editorial VARCHAR(100),
    Ventas_NA VARCHAR(100),
	Ventas_EU VARCHAR(100),
	Ventas_JP VARCHAR(100),
	Ventas_Otros VARCHAR(100),
	Ventas_Global VARCHAR(100)
);


SELECT COUNT(*) AS TOTAL_GENERAL FROM VideoJuego1;

SELECT * FROM VideoJuego1

