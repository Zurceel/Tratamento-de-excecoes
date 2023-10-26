if __name__ == '__main__':
    produtosDisponiveis = ['Laranja', 'Suco', 'Carne', 'Refrigerante']
    listaProdutos = []
    produto = None

    while True:
        produto = input('Digite o produto que deseja: (Digite 0 para finalizar)')

        if produto == '0':
            break

        if produto in produtosDisponiveis:
            listaProdutos.append(produto)
        else:
            print(f'O produto {produto}  não esta disponível')


    print('Produtos Disponíveis:')
    print(sorted(produtosDisponiveis))

    print('Produtos comprados:')
    print(listaProdutos)