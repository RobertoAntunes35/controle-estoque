
$(document).ready(function() {
    $('#btnBuscar').click(function(event) {
        event.preventDefault();

        var inputValue = $('#codigo').val();
        console.log(inputValue);

    $.ajax({
        url: '/busca_produtos',
        type: 'POST',
        data: {codigoProduto: inputValue},
        success: function(date) {
            $('#descricao').val(date.updatedValue.descricao)
            $('#codigoFornecedor').val(date.updatedValue.codigoFornecedor)
            $('#unidade').val(date.updatedValue.unidade)
        }
    });
    });
});


function verificarEnter(event) {
    if(event.keyCode === 13) {
        event.preventDefault();

        var botao = document.getElementById("#btnBuscar")
        botao.click();
    }
}