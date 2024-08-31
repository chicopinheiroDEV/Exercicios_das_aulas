vendas_totais = {
    "ProdutoA": 4798,
    "ProdutoB": 3998,
    "ProdutoC": 3999,
    "ProdutoD": 4798,
    "ProdutoE": 2249
}

maximo = max(vendas_totais.values())

produto_mais_vendido = []
for produto, vendas in vendas_totais.items():
    if vendas == maximo:
        produto_mais_vendido.append(produto)

print(produto_mais_vendido)
