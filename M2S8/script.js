/* var numero = parseInt(prompt("Ingrese un número"));
for (var inicio = 1; inicio <= numero; inicio++) { //inicio++ incrementa 1 unidad, equivale a inicio += 1
    console.log(inicio); */
// } //si el numero es 0, no se ejecuta porque no entra en el bucle for; no se cumple la condicion de que numero debe ser ser igual o mayor a 1
// si uno pone let en vez de var, el valor de numero queda indefinido, porque el scope de let tiene alcance de bloque, no sirve para otras iteraciones.

/* let dividendo = parseInt(prompt("Ingresa el dividendo:"));
let divisor = parseInt(prompt("Ingresa el divisor:"));
try{
    if(divisor === 0)
        throw new Error("Divide por 0");
    console.log("El cuociente es: " + dividendo/divisor);
}catch (err){
    console.log(err);
}finally{
    console.log("Fin del Programa");
} */
/* 
    var numero = 10; try { if(numero != 7) throw new Error("El número no es 7"); } catch (error) { console.log(error.name, error.message) } console.log("continua la ejecución del programa")

/*     let frutas = ["manzana", "plátano", "pera"];
for (let fruta of frutas) {
    console.log(fruta);
} */

/* var paises = ["Chile", "Argentina", "Paraguay"];
console.log(paises);


let persona = {
    nombre: "Juan",
    edad: 35,
    profesion: "Ingeniero", saludar: function () {
        console.log("!Hola, soy " + this.nombre + "!");
    }
};
persona.saludar(); */

var perro = {
    nombre: "Firulais",
    edad: 4,
    sexo: "M",
    raza: "husky siberiano",
    ladrar: function () {
        console.log("guau XD!");
    },
    comer: function () {
        console.log("Crunchcrunch");
    },
    dormir: function() {
        console.log("Zzz...");
    },}
    