CREATE TABLE empresa (
	rut VARCHAR (10) PRIMARY KEY,
	nombre VARCHAR (120) NOT NULL,
	direccion VARCHAR (120),
	telefono VARCHAR (15),
	correo VARCHAR (80),
	web VARCHAR (50)
);

CREATE TABLE clientes (
	rut VARCHAR (10) PRIMARY KEY,
	nombre VARCHAR (120) NOT NULL,
	correo VARCHAR (80),
	direccion VARCHAR (120),
	celular VARCHAR (15)
);

CREATE TABLE herramientas (
	id_herramienta NUMERIC (12) PRIMARY KEY,
	nombre VARCHAR (120) NOT NULL,
	precio_dia NUMERIC (12)
);

CREATE TABLE arriendos (
	folio NUMERIC (12) PRIMARY KEY,
	fecha DATE,
	dias NUMERIC (5) NOT NULL,
	valor_dia NUMERIC (12),
	garantia VARCHAR (30),
	herramienta_idHerramienta NUMERIC (12),
	cliente_rut VARCHAR (10)
);

-- DROP TABLE empresa, cliente, herramienta, arriendo;

ALTER TABLE arriendos ADD CONSTRAINT fk_herramienta_idHerramienta
	FOREIGN KEY (herramienta_idHerramienta)
	REFERENCES herramientas(id_herramienta);

ALTER TABLE arriendos ADD CONSTRAINT fk_cliente_rut
	FOREIGN KEY (cliente_rut)
	REFERENCES clientes(rut); -- query returned hasta acá

INSERT INTO empresa (rut, nombre, direccion, telefono, correo, web)
VALUES ('87654321-9','HolaMundo', 'San Martín 642', '913313210','chaomundo@mail.cl','www.holamundo.org');

INSERT INTO clientes (rut, nombre, correo, direccion, celular)
VALUES 
    ('12345678-9', 'Pedro Pérez', 'pedro.perez@mail.com', 'Av. Vicuña Mackenna 100', '912345678'),
    ('23456789-0', 'Juanín Juan', 'juanin@mail.cl', 'Ministro Carvajal', '923456789'),
    ('34567890-1', 'Diego Díaz', 'diego.noches@mail.com', 'Av. Libertador Bernardo Ohiggins 10', '934567890');

INSERT INTO herramientas (id_herramienta, nombre, precio_dia)
VALUES 
    (1001, 'Taladro Manual', 30.00),
    (1002, 'Sierra Cuadrada', 40.00),
    (1003, 'Descompresor de Aire', 75.50),
    (1004, 'Lijadora', 12.75),
    (1005, 'Martillo Neumático', 90.00); -- segunda query returned hasta acá

-- Borrar último cliente (Diego) y primera herramienta (taladro)
DELETE FROM clientes
WHERE rut = '34567890-1';

DELETE FROM herramientas
WHERE id_herramienta = 1001;

-- Arriendo para Pedro
INSERT INTO arriendos (folio, fecha, dias, valor_dia, garantia, herramienta_idHerramienta, cliente_rut)
VALUES 
    (10001, '2024-09-01', 3, 40.00, 'Depósito bancario', 1002, '12345678-9'),
    (10002, '2024-09-15', 4, 75.50, 'Tarjeta de crédito', 1003, '12345678-9');

-- arriendo para Juanín
INSERT INTO arriendos (folio, fecha, dias, valor_dia, garantia, herramienta_idHerramienta, cliente_rut)
VALUES 
    (10003, '2024-09-05', 2, 30.00, 'Efectivo', 1004, '23456789-0'),
    (10004, '2024-09-20', 5, 90.00, 'Depósito bancario', 1005, '23456789-0');

-- arriendo para Diego
INSERT INTO arriendos (folio, fecha, dias, valor_dia, garantia, herramienta_idHerramienta, cliente_rut)
VALUES 
    (10005, '2024-09-10', 4, 12.75, 'Tarjeta de crédito', 1004, '34567890-1'),
    (10006, '2024-09-25', 5, 75.50, 'Efectivo', 1003, '34567890-1');

-- Pedro cambia de correo
UPDATE clientes
SET correo = 'nuevo.pedro.perez@mail.com'
WHERE rut = '12345678-9';

-- ver herramientas
SELECT * FROM herramientas

--ver arriendos de segundo cliente (juanín)
SELECT * FROM arriendos
WHERE cliente_rut = '23456789-0';

--ver clientes con alguna a en el nombre
SELECT * FROM clientes
WHERE nombre ILIKE '%A%'; -- ILIKE para que salgan con y sin mayus

--obtener nombre de segunda herramienta insertada (Sierra Cuadrada)
SELECT * FROM herramientas
WHERE id_herramienta = 1002;

-- modificar primeros dos arriendos con nueva fecha: 15/01/2000 (al revés)
UPDATE arriendos
SET fecha = '2000-01-15'
WHERE folio IN (10001, 10002);

SELECT * FROM arriendos
WHERE cliente_rut = '12345678-9';

-- mostrar folio, fecha y valor_dia de arriendos de enero 2020
SELECT * FROM arriendos
WHERE fecha = '2000-01-15';