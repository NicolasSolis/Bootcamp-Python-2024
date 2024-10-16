BEGIN; -- crear tablas
CREATE TABLE departamentos (
	id INTEGER PRIMARY KEY,
	nombre VARCHAR (100),
	ubicacion VARCHAR (100)
);

CREATE TABLE empleados (
	id INTEGER PRIMARY KEY,
	nombre VARCHAR (100),
	puesto VARCHAR (100),
	salario DECIMAL (10, 2),
	fecha_contratacion DATE,
	departamento_id INTEGER
);

ALTER TABLE empleados
ADD CONSTRAINT fk_departamento_id
FOREIGN KEY (departamento_id)
REFERENCES departamentos (id);

COMMIT;

-- modificar tablas
ALTER TABLE empleados
ADD COLUMN email VARCHAR(100);

ALTER TABLE empleados RENAME TO trabajadores;

DROP TABLE departamentos CASCADE;