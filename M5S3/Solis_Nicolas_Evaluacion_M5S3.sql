CREATE DATABASE ev_m5s3
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE empresa (
	rut VARCHAR (10) PRIMARY KEY,
	nombre VARCHAR (120) NOT NULL,
	direccion VARCHAR (120),
	telefono VARCHAR (15),
	correo VARCHAR (80),
	web VARCHAR (50)
);

CREATE TABLE cliente (
	rut VARCHAR (10) PRIMARY KEY,
	nombre VARCHAR (120) NOT NULL,
	correo VARCHAR (80),
	direccion VARCHAR (120),
	celular VARCHAR (15)
);

CREATE TABLE herramienta (
	id_herramienta NUMERIC (12) PRIMARY KEY,
	nombre VARCHAR (120) NOT NULL,
	precio_dia NUMERIC (12)
);

CREATE TABLE arriendo(
	folio NUMERIC (12) PRIMARY KEY,
	fecha DATE,
	dias NUMERIC (5) NOT NULL,
	valor_dia NUMERIC (12),
	garantia VARCHAR (30),
	herramienta_idHerramienta NUMERIC (12),
	cliente_rut VARCHAR (10)
);

ALTER TABLE arriendo ADD CONSTRAINT fk_herramienta_idHerramienta
	FOREIGN KEY (herramienta_idHerramienta)
	REFERENCES herramienta(id_herramienta);

ALTER TABLE arriendo ADD CONSTRAINT fk_cliente_rut
	FOREIGN KEY (cliente_rut)
	REFERENCES cliente(rut);