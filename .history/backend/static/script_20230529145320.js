

$(document).ready(function() {
    $("#busca-produto").click(function(event) {
        event.preventDefault();
        var itemID = $("#busca-produto").val();
        window.location.href = "/teste/"+itemID
    })
})
