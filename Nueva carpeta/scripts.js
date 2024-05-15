function mostrar_hora(){

    var ahora = new Date()
    var horas = ahora.getHours()
    var minutos = ahora.getMinutes()
    var segundos = ahora.getSeconds()
    var hora_actual = horas + ":" + minutos +":" + segundos
    document.getElementById("Hola").innerText = 'La hora actual es: ' + hora_actual
}
setInterval(mostrar_hora, 1000);
mostrar_hora();