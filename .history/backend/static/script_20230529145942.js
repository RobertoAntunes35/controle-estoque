



function redirecionar () {
    var itemID = document.getElementById("codigo-produto").value;
    var url = "/teste?item_id=" + encodeURIComponent(itemID)
    console.log(itemID)
}