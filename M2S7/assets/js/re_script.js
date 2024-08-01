let numero1, numero2;
numero1 = prompt("Por favor ingrese el primer número");
numero2 = prompt("Por favor ingrese un segundo número");
numero1 = parseInt(numero1);
numero2 = parseInt(numero2);
if (numero1 > numero2) {
    alert(numero1 + " es mayor que " + numero2);
}
if (numero1 < numero2) {
    alert(numero1 + " es menor que " + numero2);
}
if (numero1 == numero2) {
    alert(numero1 + " es igual que " + numero2);
}