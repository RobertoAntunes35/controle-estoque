



function busca_produto () {
    var itemID = document.getElementById("codigo-produto").value;
    var url = "/teste?item_id=" + encodeURIComponent(itemID);
    window.location.href = url;
    console.log(itemID)
}

function busca_cliente() {
    var clienteID = document.getElementById("")
}