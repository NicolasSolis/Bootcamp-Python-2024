CREATE DATABASE peliculas
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE peliculas (
	id INTEGER PRIMARY KEY,
	pelicula VARCHAR (100),
	estreno SMALLINT,
    director VARCHAR (100)
);

CREATE TABLE reparto (
	id SERIAL PRIMARY KEY,
    id_pelicula SMALLINT,
    actor VARCHAR (100)
);

ALTER TABLE reparto
ADD CONSTRAINT fk_id_pelicula
FOREIGN KEY (id_pelicula)
REFERENCES peliculas (id);

SELECT * FROM peliculas;
SELECT * FROM reparto;

-- DROP TABLE peliculas, reparto;

-- listar actores de titanic con titulo pelicula, año estreno, director y reparto

-- listar top 10 directores populares, (nombre y cantidad de peliculas)

-- cuántos actores hay

-- listar estrenos entre 1990 y 1999 (incluir ambos) ordenados por titulo, ascendente

-- listar actores película más nueva

-- insertar datos de nueva película con rollback y otra definitiva

-- actualizar (update) 5 directores con rollback

-- insertar 3 actores en "Rambo" ocupando savepoint (?)

-- eliminar estrenos de pelicula año 2008 con rollback

-- insertar 2 actores en cada película del 2001 de verdad

-- udpdate set película "King Kong" a "Donkey kong" con rollback