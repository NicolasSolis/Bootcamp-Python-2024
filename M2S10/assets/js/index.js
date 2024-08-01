//typeof(miTexto) es un string por alguna razón

/* $(document).ready(function () {
    
    var miTexto = $("#contenido").text();
    alert(miTexto);

}) */
/* $(document).ready(function () {
    var miAtributo = $("#nombre").attr("type");
    alert(miAtributo);
}) */
/* text equivale a innerText */

/* $(document).ready(function () {
    $("#caja1").mouseenter(function () {
        $("#caja2").show();
    })
}) */

/* $("#caja1").mouseenter(function () { $("#caja2").toggle(); 
}) */

/* var clickTimer = null;

function touchStart() {
    if (clickTimer == null) {
        clickTimer = setTimeout(function () {
            clickTimer = null;
            alert("single");

        }, 500)
    } else {
        clearTimeout(clickTimer);
        clickTimer = null;
        alert("double");

    }
}

$("#boton").click(function () {
    var nombre = $("#nombre").val(); var correo = $("#correo").val();
    alert("su nombre es: " + nombre + " y su correo es: " + correo);
})
$("#boton1").click(function () {
    $("#contenido").css("background-color", "greenyellow");
})
$("#boton2").click(function () {
    $("#texto").text("Texto escrito usando JQuery");

})
$("#boton1").dblclick(function () {
    $("#contenido").css("background-color", "white");
    $("#texto").text("Lorem, ipsum dolor sit amet consectetur adipisicing elit. Repudiandae voluptatibus" + "doloremque rerum corrupti eveniet, quis quas nam quisquam," + "magnam consequuntur ipsa aspernatur reprehenderit repellendus delectus voluptates veniam" + "odio, adipisci aliquam!");
}) */