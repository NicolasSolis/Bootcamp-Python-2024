/* tiene la maña de necesitar apretar los botones más de una vez (no dobleclick)
para que "cargue" el script, function, o de alguna modificación directa en el DOM.
Intenté algunas formas de inicializarlo, pero internet aconseja que no, su funcionalidad es la misma y lo dejé tal cual.
ocupé MUCHAS herramientas porque me cuesta javascript; las más utiles pythontutor y html-cleaner/js, 
Gracias Victor por el material*/
let tareasArr = [{
    tarea: "Pintar la fachada de la casa"
}, {
    tarea: "Comprar comida para el perro"
}, {
    tarea: "Pagar la tarjeta de crédito"
}]

const btnMostrarForm = document.getElementById("btnMostrarForm");
const formTarea = document.getElementById("formTarea");
const submitTarea = document.getElementById("submitTarea");
const tablaTareas = document.getElementById("tabla-tareas");
const cuerpoTabla = document.getElementById("cuerpo-tabla");

//toggle para mostrar botón Agregar tarea v2
btnMostrarForm.addEventListener("click", () => {
    formTarea.style.display = formTarea.style.display === "none" ? "block" : "none"
});

//ver array en tabla
function verTabla() {
    cuerpoTabla.innerHTML = "";
    tareasArr.forEach((tarea) => {
        let nueva = document.createElement("tr");
        nueva.innerHTML = `
        <td>${tarea.tarea}</td>
        <td><button class="btn btn-danger">Finalizar</button></td>`;
        cuerpoTabla.appendChild(nueva);
    });
}

//añadir tarea a array, y eso a tabla
submitTarea.addEventListener("click", () => {
    let tareaInput = document.getElementById("agregarTarea");
    let tareaValue = tareaInput.value;

    if (tareaValue !== "") { //para atajar espacios en blanco (lo estaba haciendo al revés)
        let tareaObj = {
            tarea: tareaValue
        };
        tareasArr.push(tareaObj);
        tareaInput.value = "";
    } else {
        alert("Por favor ingrese una tarea")
    }
    verTabla();
});

cuerpoTabla.addEventListener("click", () => {
    let btnFinalizar = document.querySelectorAll(".btn-danger");
    if (btnFinalizar) {
        btnFinalizar.forEach((btn, index) => {
            btn.addEventListener("click", () => {
                tareasArr.splice(index, 1);
                verTabla();
            });
        });
    }
})

verTabla();