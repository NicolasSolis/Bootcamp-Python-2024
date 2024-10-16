BEGIN; -- inicio crear tablas

CREATE TABLE editoriales (
	codigo SERIAL PRIMARY KEY,
	nombre VARCHAR (32)
);

CREATE TABLE libros (
	codigo SERIAL PRIMARY KEY,
	titulo VARCHAR (32),
	codigoeditorial SERIAL
);

;
ALTER TABLE libros
ADD CONSTRAINT fk_codigoeditorial
FOREIGN KEY (codigoeditorial)
REFERENCES editoriales (codigo);

-- insertar datos a tablas

INSERT INTO editoriales (nombre)
VALUES 
	('Anaya'),
	('Andina'),
	('S.M.');


INSERT INTO libros (titulo, codigoeditorial)
VALUES 
	('Don Quijote de La Mancha I', 1),
	('El principito', 2),
	('El príncipe', 3),
	('Diplomacia', 3),
	('Don Quijote de La Mancha II', 1);

COMMIT; -- fin crear tablas

-- revisar
SELECT * FROM libros
INNER JOIN editoriales
ON libros.codigoeditorial = editoriales.codigo;

-- inicio modificar tabla libros agregando autor y precio
BEGIN;

ALTER TABLE libros
ADD COLUMN autor VARCHAR (32),
ADD COLUMN precio INTEGER;


-- insertar autor y precio a libros ya ingresados
UPDATE libros
SET autor = (
    CASE titulo
        WHEN 'Don Quijote de La Mancha I' THEN 'Miguel de Cervantes'
        WHEN 'El principito' THEN 'Antoine SaintExupery'
        WHEN 'El príncipe' THEN 'Maquiavelo'
        WHEN 'Diplomacia' THEN 'Henry Kissinger'
        WHEN 'Don Quijote de La Mancha II' THEN 'Miguel de Cervantes'
    END
),
precio = (
    CASE titulo
        WHEN 'Don Quijote de La Mancha I' THEN 150
        WHEN 'El principito' THEN 120
        WHEN 'El príncipe' THEN 180
        WHEN 'Diplomacia' THEN 170
        WHEN 'Don Quijote de La Mancha II' THEN 140
    END
);
SAVEPOINT tablas_modificadas;

-- insertar nuevos libros
INSERT INTO libros (titulo, autor, precio)
VALUES
	('La Máquina del Tiempo', 'H.G. Wells', 150),
	('El Túnel', 'Ernesto Sábato', 160);

COMMIT;

-- eliminar en memoria libros de Anaya (fk 1) y cambio de nombres editorial, pero de mentira

BEGIN;
DELETE FROM libros WHERE codigoeditorial = 1;
-- así queda
SELECT * FROM libros INNER JOIN editoriales
ON libros.codigoeditorial = editoriales.codigo;

ROLLBACK;


-- cambio nombre editorial
BEGIN;
UPDATE editoriales 
SET nombre = 'Mountain'
WHERE nombre = 'S.M.';

SAVEPOINT cambio_editorial;

SELECT * FROM editoriales WHERE nombre = 'Mountain';

UPDATE editoriales 
SET nombre = 'Iberlibro'
WHERE nombre = 'Andina';

ROLLBACK TO cambio_editorial;
COMMIT;

-- DROP TABLE editoriales, libros;