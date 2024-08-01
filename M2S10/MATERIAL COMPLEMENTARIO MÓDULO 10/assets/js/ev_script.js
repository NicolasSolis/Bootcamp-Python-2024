//dejo las const acá como prueba de mi fracaso

/* const btnVerMas = document.querySelectorAll("#detallesBaires, #detallesRio, #detallesMachuPicchu")
const detalles = document.querySelectorAll(".detalles"); */

$(document).ready(function () {
  $(".text-body-secondary").click(function () {
    var idBoton = $(this).attr("id");
    toggledCard = $("#detalles" + idBoton);
    toggledCard.toggle();
  });

  // arreglado, falta el fondo aparte
  // descubrí que si apreto ver más, y con una card abierta apreto el ver más de otra card, funciona raro
  $(".btn-close").click(function () {
    if (toggledCard) {
      toggledCard.hide()
    }
  });
});