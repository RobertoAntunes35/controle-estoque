import tkinter as tk
from tkinter import messagebox

def inserir_produto():
    # Função para tratar o evento de inserção do produto
    nome = entry_nome.get()
    preco = entry_preco.get()
    
    # Aqui você pode adicionar a lógica para inserir o produto no banco de dados ou em outra estrutura de dados
    # Por exemplo, imprimir os valores inseridos:
    print("Nome: ", nome)
    print("Preço: ", preco)
    
    # Exibir uma mensagem de sucesso
    messagebox.showinfo("Sucesso", "Produto inserido com sucesso!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Inserir Produto")

# Rótulo e campo de entrada para o nome do produto
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

# Rótulo e campo de entrada para o preço do produto
label_preco = tk.Label(janela, text="Preço:")
label_preco.pack()
entry_preco = tk.Entry(janela)
entry_preco.pack()

# Botão de inserção do produto
botao_inserir = tk.Button(janela, text="Inserir", command=inserir_produto)
botao_inserir.pack()

# Executar a janela principal
janela.mainloop()

