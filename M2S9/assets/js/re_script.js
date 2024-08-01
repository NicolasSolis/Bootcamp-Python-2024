/* 
• Al pasar el mouse por el primer <div> “text1” se mostrará el segundo (asumo que se refiere al text2) y al salir de él (asumo que es onmouseout) se ocultará nuevamente. 
• Al hacer clic en el <div> id “caja2” la imagen deberá agrandarse un 100% y al salir de ella, volver a su tamaño inicial. 
• Con el tercer <div> la letra se agrandará al hacer doble clic en él.
• La imagen seleccionada para el trabajo es irrelevante.
*/
function ocultarSegundo(){
    document.getElementById("text2").style.display = "none";
}
function mostrarSegundo(){
    document.getElementById("text2").style.display = "block";
}
function zoomImg(){
    document.getElementById("img").style.width = "100%";
}
function zoomOutImg(){
    document.getElementById("img").style.width = "20%";
}
function zoomText(){
    document.getElementById("caja3").style.fontSize = "25px";
}