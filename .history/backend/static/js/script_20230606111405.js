
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


// function verificarEnter(event) {
//     if(event.keyCode === 13) {
//         event.preventDefault();

//         var botao = document.getElementById("btnBuscar")
//         botao.click();
//     }
// }


// Busca produtos 
$(document).ready(function() {
    $('#btnBuscaProduto').click(function (event) {
        event.preventDefault();

        var valueCodigoProduto = $('#codigoProdutoBusca').val()
        console.log(valueCodigoProduto);

        $.ajax({
            url:'/busca_produtos',
            type:'POST',
            data: {codigoProduto : valueCodigoProduto},
            success: function(date) {
                $('#descricaoProduto').val(date.updatedValueProduto.descricao)
                $('#valorVenda').val(date.updatedValueProduto.valorVenda)
                $('#unidadeProduto').val(date.updatedValueProduto.unidade)
            }
        })
    } )
})

// Busca Cliente
$(document).ready(function() {
    $('#btnBuscaClientes').click(function (event) {
        event.preventDefault();

        var valueClienteBusca = $('#codigoCliente').val()
        console.log(valueClienteBusca)

        $.ajax({
            url:'/buscar_clientes',
            type:'POST',
            data: {codigoCliente : valueClienteBusca},
            success: function(date) {
                $('#nomeFantasia').val(date.updateValueCliente.nomeFantasia)
                $('#enderecoCliente').val(date.updateValueCliente.endereco)
                $('#cidadeCliente').val(date.updateValueCliente.cidade)
                $('#dataEntrega').val(Date.now())
            }
        })
    })
})