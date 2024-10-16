BEGIN;
CREATE USER Juan WITH PASSWORD 'pass1'; -- con esto es suficiente para saber que hay transacción en curso

COMMIT; -- confuso

DROP USER Juan;

BEGIN;
CREATE USER Pedro WITH PASSWORD 'pass2';
-- ROLLBACK; -- comentado para poder engendrar a Pedro
COMMIT; -- error porque ya no hay transacción en curso si hay rollback

DROP USER Pedro; -- no existe por el rollback

SELECT usename, usesysid FROM pg_user; -- ocupar * para todo
-- hasta acá llega lo de usuarios, siguen tablas

BEGIN; -- se les agrega BEGIN y COMMIT para gestionar transacciones
CREATE TABLE producto (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	precio SMALLINT
);

-- ROLLBACK; -- entre creación tablas, solo crea una tabla cuentas porque existe este rollback, comentada para que fucione crear pedro
COMMIT;
CREATE TABLE cuentas (
	n_cuenta NUMERIC PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	balance REAL
);

COMMIT;

-- Se siguen insertando datos en cuenta, pide activar autocommit, no es necesario realmente

INSERT INTO cuentas (n_cuenta, nombre, balance)
VALUES (148, 'Pepe', 2000);
UPDATE cuentas SET balance = balance - 137.0 WHERE nombre = 'Pepe' -- resta 137 a las cuentas donde el nombre sea Pepe
-- efectivamente funcionó

-- Ahora se le insertan datos en producto, ocupando begin y commit,
-- finalmente desactivando autocommit

BEGIN;
INSERT INTO producto (id, nombre, precio)
VALUES (1, 'Zapato', 1000);

INSERT INTO producto (id, nombre, precio)
VALUES (2, 'Polera', 500);

INSERT INTO producto (id, nombre, precio)
VALUES (3, 'Pantalón', 700);
COMMIT;
-- funcionó, hay que revisar tablas, bd>schemas>tables>click derecho en la tabla> view/edit data> all rows
-- ahora actualizar datos ocupando savepoint

BEGIN;
UPDATE producto SET precio = precio + 100.25 WHERE nombre = 'Zapato'; -- valor añadido es real, tipo de dato precio es smallint, se trunca el valor añadido
SAVEPOINT sp; -- solo guarda desde el begin hasta este punto

UPDATE producto SET precio = precio - 180.50
WHERE nombre = 'Polera';
ROLLBACK TO SAVEPOINT sp; -- no aplica cambios después del savepoint 'sp'

COMMIT;
-- Precio de poelra sin cambios, ROLLBACK revierte hasta 'sp', deshace actualizaciones post-savepoint, en este caso update precio polera