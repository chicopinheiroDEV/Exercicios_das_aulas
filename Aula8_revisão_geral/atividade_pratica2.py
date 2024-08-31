estoque = {
    'energético': {'preço': 10, 'qtd': 5},
    'whey protein': {'preço': 140, 'qtd': 10}
}

def add_itens():
    produto = input('Informe o produto: ')
    preco = float(input('Digite o preço do produto: '))
    qtd = int(input('Digite a quantidade: '))

    estoque[produto] = {
        'preço': preco, 
        'qtd': qtd 
    }

add_itens()

def remove_itens(produto):
    del estoque[produto]

remove_itens('energético')
print(estoque)