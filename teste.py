from repositorio_cardapio import RepositorioCardapio
from repositorio_produto import RepositorioProduto

print()

repo_cardapio = RepositorioCardapio('db.sqlite')
repo_produto = RepositorioProduto('db.sqlite')

cardapio = repo_cardapio.criar_cardapio('bebidas', 'Bebidas', 'Bebidas da casa')
produto = repo_produto.criar_produto('coca-cola', 'bebidas', 'Coca Cola', 'Coca Cola 2L', '9.80', 'vegano')

cardapio = repo_cardapio.consultar_cardapio('bebidas')
produto = repo_produto.consultar_produto('coca-cola')
print(cardapio, '\n')
print(produto, '\n')

alterados = repo_cardapio.alterar_cardapio('bebidas', 'Bebidas', 'Novo cardápio de bebidas')
alterados = repo_produto.alterar_produto('coca-cola', 'bebidas', 'Coca Cola', 'Nova Coca Cola 2.5L', '9.80', 'vegano')

cardapio = repo_cardapio.consultar_cardapio('bebidas')
produto = repo_produto.consultar_produto('coca-cola')
print(cardapio, '\n')
print(produto, '\n')

removidos = repo_produto.remover_produto('coca-cola')
removidos = repo_cardapio.remover_cardapio('bebidas')

cardapios = repo_cardapio.consultar_todos_cardapios()
produtos = repo_produto.consultar_todos_produtos()
print(cardapios, '\n')
print(produtos, '\n')