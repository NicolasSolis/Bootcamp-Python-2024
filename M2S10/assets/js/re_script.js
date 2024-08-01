$(document).ready(function () {
    $("#text2").hide();  //se ve raro sin esto, lo dejé

    $("#text1").mouseover(function () {
        $("#text2").show();
    })
    $("#text1").mouseleave(function () {
        $("#text2").hide();
    })
    $("#caja2").click(function () {
        $(img).toggleClass("imagenGrande");
    })
    $("#caja3").dblclick(function () {
        $(this).toggleClass("letraGrande")
    })
})
