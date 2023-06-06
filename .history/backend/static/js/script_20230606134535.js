
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
            url:'/busca_clientes',
            type:'POST',
            data: {codigoCliente : valueClienteBusca},
            success: function(date) {
                $('#nomeFantasia').val(date.updatedValueCliente.nomeFantasia)
                $('#enderecoCliente').val(date.updatedValueCliente.endereco)
                $('#cidadeCliente').val(date.updatedValueCliente.cidade)
                $('#dataEntrega').val(date.updatedValueCliente.dataEntrega)
                $('#vendedorResponsavel').val(date.updatedValueCliente.vendedorResponsavel)
            }
        })
    })
})


// Adicionando dados a tabela

$(document).ready(function () {
    $('#btnAdicionarItem').click(function (event) {
        // event.preventDefault();

        var codigoProduto = $('#codigoProdutoBusca').val()
        var nomeProduto = $('#descricaoProduto').val()
        var quantidadeProduto = $('#quantidadeProduto').val()
        var unidadeProduto = $('#unidadeProduto').val()
        var valorProduto = $('#valorVenda').val()

        let valorTotal = parseFloat(valorProduto) * parseInt(quantidadeProduto)

        valorTotal.toFixed(3)

        $.ajax({
            url:'/adicionar_item_tabela',
            type:'POST',
            data: {
                codigoProduto: codigoProduto,
                nomeProduto: nomeProduto,
                quantidadeProduto: quantidadeProduto,
                unidadeProduto: unidadeProduto,
                valorProduto:valorProduto,
                valorTotal: valorTotal
            },
            success: function(data) {
                var newRow = $('<tr>');
                newRow.append('<th scope="row">' + 1 + '</th>')
                newRow.append('<td>' + data.codigoProduto + '</td>')
                newRow.append('<td>' + data.nomeProduto + '</td>')
                newRow.append('<td>' + data.quantidadeProduto + '</td>')
                newRow.append('<td>' + data.unidadeProduto + '</td>')
                newRow.append('<td>' + data.valorTotal + '</td>')
                newRow.append('<td>' + '<a href="#"> Editar </a>' + '</td>' )
                $('#tableProdutosPedido tbody').append(newRow)
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        })

    })
})