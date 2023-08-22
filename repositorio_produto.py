from typing import List
from repositorio import Repositorio
from produto import Produto

class RepositorioProduto(Repositorio):

    def __init__(self, nome_db: str) -> None:
        super().__init__(nome_db)

    @staticmethod
    def montar_produto(tupla_dados: tuple) -> Produto:
        codigo, codigo_cardapio, nome, descricao, preco, restricao = tupla_dados
        preco = float(preco)
        return Produto(codigo, codigo_cardapio, nome, descricao, preco, restricao)
    
    def criar_produto(self, codigo: str, codigo_cardapio: str, 
        nome: str, descricao: str, preco: float, restricao: str) -> int:
        query = 'INSERT INTO produto (codigo, codigo_cardapio, nome, descricao, preco, restricao) VALUES (?, ?, ?, ?, ?, ?);'
        self.abrir_conexao()
        self.cursor.execute(query, (codigo, codigo_cardapio, nome, descricao, preco, restricao))
        self.connection.commit()
        return self.obter_mudancas_fechar()
    
    def consultar_produto(self, codigo: str) -> Produto:
        query = 'SELECT codigo,codigo_cardapio,nome,descricao,preco,restricao FROM produto WHERE codigo = ?;'
        self.abrir_conexao()
        self.cursor.execute(query, (codigo,))
        produto = self.cursor.fetchone()
        self.fechar_conexao()
        return self.montar_produto(produto) if produto else produto
    
    def consultar_todos_produtos(self, preco_min: int = -1, preco_max: int = 99999, 
            codigo_cardapio: str = '', restricao: str = '') -> List[Produto]:
        
        query = 'SELECT codigo,codigo_cardapio,nome,descricao,preco,restricao FROM produto WHERE preco >= ? AND preco <= ?'

        parametros = [preco_min, preco_max]

        if codigo_cardapio:
            query += ' AND codigo_cardapio = ?'
            parametros.append(codigo_cardapio)

        if restricao:
            query += ' AND restricao = ?'
            parametros.append(restricao)

        query += ';'
        
        self.abrir_conexao()
        self.cursor.execute(query, tuple(parametros))
        produtos = self.cursor.fetchall()
        self.fechar_conexao()
        return [self.montar_produto(produto) for produto in produtos]
    
    def alterar_produto(self, codigo: str, codigo_cardapio: str, 
        nome: str, descricao: str, preco: float, restricao: str) -> int:
        query = 'UPDATE produto SET codigo_cardapio = ?, nome = ?, descricao = ?, preco = ?, restricao = ? WHERE codigo = ?'
        self.abrir_conexao()
        self.cursor.execute(query, (codigo_cardapio, nome, descricao, preco, restricao, codigo))
        self.connection.commit()
        return self.obter_mudancas_fechar()
    
    def remover_produto(self, codigo: str) -> int:
        query = 'DELETE FROM produto WHERE codigo = ?'
        self.abrir_conexao()
        self.cursor.execute(query, (codigo,))
        self.connection.commit()
        return self.obter_mudancas_fechar()
