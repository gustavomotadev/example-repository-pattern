class Cardapio(object):
    
    def __init__(self, codigo: str, nome: str, descricao: str) -> None:
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        
    def __repr__(self) -> str:
        return f'Cardapio("{self.codigo}","{self.nome}","{self.descricao}")'
    
    def __str__(self) -> str:
        return f'Cardapio("{self.codigo}","{self.nome}","{self.descricao}")'
    