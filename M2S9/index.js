/* var selectorId = document.getElementById("parrafo").innerHTML;
var selectorTag = document.getElementsByTagName("h1");
var selectorClass = document.getElementsByClassName("contenedor");
var selectorVarios = document.querySelector(".contenedor");
var selectorTodos = document.querySelectorAll(".contenedor");

var creandoElemento = document.createElement("p");
creandoElemento.textContent = "Este nodo fue creado desde Javacript";
document.body.appendChild(creandoElemento);

var selectorVarios = document.querySelector(".contenedor");
var creandoElemento = document.createElement("p");
creandoElemento.textContent = "Este nodo fue creado desde JavaScript";
selectorVarios.append(creandoElemento);
//cuando creamos un elemento, este no es reutilizable. Pero sí se puede redefinir, aparentemente.

var creandoElemento = document.createElement("p");
creandoElemento.textContent = "Este nodo fue creado desde Javacript nuevamente";
selectorClass[1].appendChild(creandoElemento);

var nodoPadre = document.querySelector(".contenedor");
var nodoHijo = document.querySelector("#parrafo");
nodoPadre.removeChild(nodoHijo); */

/* var texto = document.getElementById("parrafo").innerHTML="Este es el nuevo párrafo"; */ //innerHTML tb sirve para poner elementos
//inner text pone solo texto, cadena de texto
//no es necesario poner el var texto, si es que no va a ser reutilizado

function mostrarMensaje(){
    document.getElementById("caja2").style.display = "block";
}
function ocultarMensaje(){
    document.getElementById("caja2").style.display = "none";
}
function cambiarFondo(){
    document.getElementById("contenido").style.backgroundColor = "yellow";
}
function cambiarTexto(){
    document.getElementById("texto").innerText = "Chao de nuevo";
}
function volver(){
    document.getElementById("contenido").style.backgroundColor = "coral";
}

/* document.getElementById("boton2").onclick = cambiarTexto */
const boton2 = document.getElementById("boton2");
boton2.addEventListener("ondblclick", function(){});