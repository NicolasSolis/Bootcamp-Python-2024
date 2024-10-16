--BASE DE DATOS (CREATE) por Yyoyoy

CREATE TABLE proveedores(
	nombre VARCHAR(32),
	localidad VARCHAR(32) DEFAULT 'Santiago'
);

CREATE TABLE prestamos(
	idPrestamo NUMERIC(8),
	fechaPrestamo DATE DEFAULT current_date
)