from typing import List
from repositorio import Repositorio
from cardapio import Cardapio

class RepositorioCardapio(Repositorio):
        
    @staticmethod
    def montar_cardapio(tupla_dados: tuple) -> Cardapio:
        codigo, nome, descricao = tupla_dados
        return Cardapio(codigo, nome, descricao)
        
    def __init__(self, nome_db: str) -> None:
        super().__init__(nome_db)
    
    def criar_cardapio(self, codigo: str, nome: str, descricao: str) -> int:
        query = 'INSERT INTO cardapio (codigo, nome, descricao) VALUES (?, ?, ?);'
        self.abrir_conexao()
        self.cursor.execute(query, (codigo, nome, descricao))
        self.connection.commit()
        return self.obter_mudancas_fechar()
    
    def consultar_cardapio(self, codigo: str) -> Cardapio:
        query = 'SELECT codigo,nome,descricao FROM cardapio WHERE codigo = ?;'
        self.abrir_conexao()
        self.cursor.execute(query, (codigo,))
        cardapio = self.cursor.fetchone()
        self.fechar_conexao()
        return self.montar_cardapio(cardapio) if cardapio else None
    
    def consultar_todos_cardapios(self) -> List[Cardapio]:
        query = 'SELECT codigo,nome,descricao FROM cardapio;'
        self.abrir_conexao()
        self.cursor.execute(query)
        cardapios = self.cursor.fetchall()
        self.fechar_conexao()
        return [self.montar_cardapio(cardapio) for cardapio in cardapios]
    
    def alterar_cardapio(self, codigo: str, nome: str, descricao: str) -> int:
        query = 'UPDATE cardapio SET nome = ?, descricao = ? WHERE codigo = ?'
        self.abrir_conexao()
        self.cursor.execute(query, (nome, descricao, codigo))
        self.connection.commit()
        return self.obter_mudancas_fechar()
    
    def remover_cardapio(self, codigo: str) -> int:
        query = 'DELETE FROM cardapio WHERE codigo = ?'
        self.abrir_conexao()
        self.cursor.execute(query, (codigo,))
        self.connection.commit()
        return self.obter_mudancas_fechar()
