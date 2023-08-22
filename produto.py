class Produto(object):
    
    def __init__(self, codigo: str, codigo_cardapio: str, nome: str, 
        descricao: str, preco: float, restricao: str) -> None:
        self.codigo = codigo
        self.codigo_cardapio = codigo_cardapio
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.restricao = restricao
        
    def __repr__(self) -> str:
        return f'Produto("{self.codigo}","{self.nome}","{self.codigo_cardapio}","{self.descricao}","{self.preco}","{self.restricao}")'
    
    def __str__(self) -> str:
        return f'Produto("{self.codigo}","{self.nome}","{self.codigo_cardapio}","{self.descricao}","{self.preco}","{self.restricao}")'
    