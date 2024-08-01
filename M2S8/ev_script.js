/* Hay que crear objetos, minimo 3 que contengan nombre, identificador (numero de cuenta?), contraseña y saldo de cuenta
Cuando se ingrese identificador y clave y coincide, tiene que mostrar un menú con las opciones: 1.- Ver Saldo 2.- Realizar giro 3.- Realizar depósito y 4.- Salir
Menú se repite hasta que apreten salir, y si se modifica el saldo (giro o depósito) se tiene que restar o sumar */

function Usuario(nombre, id, clave, saldo) {
    this.nombre = nombre;
    this.id = id;
    this.clave = clave;
    this.saldo = saldo;
}
const usuarios = [
    new Usuario("Juan", 765890, 4567, 50000),
    new Usuario("Pedro", 777777, 8237, 80000),
    new Usuario("Diego", 744452, 7458, 34000),
    new Usuario("Prueba", 111111, 1111, 100000),
];

let usuarioValido = null;
while (!usuarioValido) {
    const usuarioInputId = prompt("Por favor ingrese su número identificador");
    const usuarioInputClave = prompt("Por favor ingrese su clave");

    for (const usuario of usuarios) {
        if (usuario.id === parseInt(usuarioInputId) && usuario.clave === parseInt(usuarioInputClave)) {
            usuarioValido = usuario;
            break;
        }
    }
    if (!usuarioValido) {
        alert("Datos incorrectos, ingrese nuevamente");
    } else {
        while (true) {
            let usuarioIngreso = parseInt(prompt(`Bienvenido ${usuarioValido.nombre}. Escribe el número de la opción que buscas: \n 1.- Ver Saldo \n 2.- Realizar giro \n 3.- Realizar depósito \n 4.- Salir`));
            switch (usuarioIngreso) {
                case 1:
                    alert(`${usuarioValido.nombre}, usted tiene un total de ${usuarioValido.saldo}`);
                    break;
                case 2:
                    const saldoGiro = parseInt(prompt("Su saldo actual es: " + usuarioValido.saldo + "\n Ingrese el monto que desea girar"));
                    if (saldoGiro > usuarioValido.saldo) {
                        alert("Usted no tiene saldo suficiente en esta cuenta");
                    } else {
                        usuarioValido.saldo -= saldoGiro;
                        alert(`Giro realizado. Su nuevo saldo es ${usuarioValido.saldo}`);
                    }
                    break;
                case 3:
                    const saldoDeposit = parseInt(prompt("Ingrese el monto que desea depositar"));
                    usuarioValido.saldo += saldoDeposit;
                    alert(`Depósito realizado. Su nuevo saldo es ${usuarioValido.saldo}`);
                    break;
                case 4:
                    alert("Gracias por preferir nuestros servicios.");
                    break;
                default:
                    alert("La opción ingresada no es válida. Gracias por preferir nuestros servicios.");
                    break;
            }
            //Era un loop infinito, se me pasó un break.
            //no era un break
            //funciona. alegría
            if (usuarioIngreso === 4)
                break;
        }
    }
}