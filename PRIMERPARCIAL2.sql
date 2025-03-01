create database PrimerParcial2;
use PrimerParcial2;

create table Countries(
Country_Code varchar(250),
Country varchar(250),
Continent varchar(250)
);

create table Population(
Country varchar(250),
Population varchar(250)
);

select * from Population;

SELECT * 
FROM Population 
ORDER BY CAST(Population AS UNSIGNED) ASC 
LIMIT 5;

SELECT c.Continent, SUM(CAST(p.Population AS UNSIGNED)) AS Total_Habitantes
FROM Population p
JOIN Countries c ON p.Country = c.Country
GROUP BY c.Continent
ORDER BY Total_Habitantes DESC;




