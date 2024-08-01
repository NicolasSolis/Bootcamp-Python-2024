/* Perdón la falta de creatividad, me robé mi trabajo de ayer */
while (numero != 5) {
    var numero = parseInt(prompt("¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Mentel. Estoy aquí para ayudarte en lo que necesites. \n Escribe el número de la opción que buscas: \n 1.- Boletas y Pagos \n 2.- Señal y llamadas \n 3.- Oferta comercial \n 4.- Otras consultas \n 5.- Salir y confirmar solicitudes"));
    switch (numero) {
        case 1:
            let opcion1 = parseInt(prompt("Seleccione una opción \n 1.- Ver Boleta \n 2.- Pagar cuenta"));
            switch (opcion1) {
                case 1:
                    alert("Haga click en aceptar para descargar su boleta");
                    break;
                case 2:
                    alert("Usted está siendo transferido. Espere por favor...");
                    break;
                default:
                    alert("La opción ingresada no es válida. Gracias por preferir nuestros servicios.");
                    break;
            }
            break;
        case 2:
            let opcion2 = parseInt(prompt("Seleccione una opción \n 1.- Problemas con la señal \n 2.- Problemas con las llamadas"));
            switch (opcion2) {
                case 1:
                case 2:
                    let solicitud = prompt("A continuación escriba su solicitud");
                    alert("Estimado usuario, su solicitud: '" + solicitud + "' \n Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos.");
                    break;
                default:
                    alert("La opción ingresada no es válida. Gracias por preferir nuestros servicios.");
                    break;
            }
            break;
        case 3:
            let opcion3 = prompt("¡Mentel tiene una oferta comercial acorde a tus necesidades! \n Para conocer más información y ser asesorado personalmente por un ejecutivo escribe 'SI' y un ejecutivo te llamará. \n De lo contrario ingrese 'NO'");
            switch (opcion3) {
                case "SI":
                case "si":
                case "Si":
                case "sI":
                    alert("Un ejecutivo se contactará con usted");
                    break;
                case "NO":
                case "no":
                case "No":
                case "nO":
                    alert("Gracias por preferir nuestros servicios");
                    break;
                default:
                    alert("La opción ingresada no es válida. Gracias por preferir nuestros servicios.");
                    break;
            }
            break;
        case 4:
            let opcion4 = prompt("A continuación escriba su consulta:")
            switch (opcion4) {
                case opcion4:
                    alert("Estimado usuario, su consulta: '" + opcion4 + "' \n Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos.");
                    break;
                default:
                    alert("La opción ingresada no es válida. Gracias por preferir nuestros servicios.");
                    break;
            }
            break;
    }
}