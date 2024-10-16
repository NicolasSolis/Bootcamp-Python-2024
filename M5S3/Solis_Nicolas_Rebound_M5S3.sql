CREATE TABLE empresa (
	rut VARCHAR (10) PRIMARY KEY,
	nombre VARCHAR (120),
	direccion VARCHAR (120),
	telefono VARCHAR (15),
	correo VARCHAR (80),
	web VARCHAR (50)
);

CREATE TABLE cliente (
	rut VARCHAR (10) PRIMARY KEY,
	nombre VARCHAR (120),
	correo VARCHAR (80),
	direccion VARCHAR (120),
	celular VARCHAR (15),
	alta CHAR (1)
);

CREATE TABLE tipo_vehiculo (
	id_tipoVehiculo NUMERIC (12) PRIMARY KEY,
	nombre VARCHAR (120)
);

CREATE TABLE marca (
	id_marca NUMERIC (12) PRIMARY KEY,
	nombre VARCHAR (120)
);

CREATE TABLE vehiculo(
	id_vehiculo NUMERIC (12) PRIMARY KEY,
	patente VARCHAR (10),
	marca VARCHAR (20),
	modelo VARCHAR (20),
	color VARCHAR (15),
	precio NUMERIC (12),
	frecuencia_mantencion NUMERIC (5),
	marca_idMarca NUMERIC (12),
	vehiculo_idTipoVehiculo NUMERIC (12)
);

ALTER TABLE vehiculo ADD CONSTRAINT fk_vehiculo_tipoVehiculo
	FOREIGN KEY (vehiculo_idTipoVehiculo)
	REFERENCES tipo_vehiculo(id_tipoVehiculo);

ALTER TABLE vehiculo ADD CONSTRAINT fk_vehiculo_marca
	FOREIGN KEY (marca_idMarca)
	REFERENCES marca(id_marca);


CREATE TABLE venta (
	folio NUMERIC (12) PRIMARY KEY,
	fecha DATE,
	monto NUMERIC (12),
	vehiculo_idVehiculo NUMERIC (12),
	cliente_rut VARCHAR (10)
);

ALTER TABLE venta
ADD CONSTRAINT fk_venta_cliente
FOREIGN KEY (cliente_rut)
REFERENCES cliente(rut);

ALTER TABLE venta
ADD CONSTRAINT fk_venta_vehiculo
FOREIGN KEY (vehiculo_idVehiculo)
REFERENCES vehiculo(id_vehiculo);

CREATE TABLE mantencion (
	id_mantencion NUMERIC (12) PRIMARY KEY,
	fecha DATE,
	trabajos_realizados VARCHAR (1000),
	venta_folio NUMERIC (12)
);

ALTER TABLE mantencion
ADD CONSTRAINT fk_mantencion_venta
FOREIGN KEY (venta_folio)
REFERENCES venta(folio);