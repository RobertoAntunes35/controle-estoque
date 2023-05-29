



function redirecionar () {
    var itemID = document.getElementById("codigo-produto").value;
    var url = "/teste/"+itemID
    window.location.href = url;
}