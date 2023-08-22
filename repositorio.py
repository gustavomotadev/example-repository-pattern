import sqlite3

class Repositorio(object):

    FOREIGN_KEY_SQLITE = 'PRAGMA foreign_keys=ON;'
    LINHAS_AFETADAS_SQLITE = 'SELECT changes();'
        
    def __init__(self, nome_db: str) -> None:
        self.nome_db = nome_db
        self.connection = None
        self.cursor = None
        
    def abrir_conexao(self) -> None:
        self.connection = sqlite3.connect(self.nome_db)
        self.cursor = self.connection.cursor()
        self.ativar_foreign_key()
        
    def fechar_conexao(self) -> None:
        self.cursor.close()
        self.connection.close()
        self.connection = None
        self.cursor = None

    def ativar_foreign_key(self) -> None:
        self.cursor.execute(self.FOREIGN_KEY_SQLITE)

    def obter_mudancas(self) -> int:
        mudancas = self.cursor.execute(self.LINHAS_AFETADAS_SQLITE)
        return mudancas.fetchone()[0]
    
    def obter_mudancas_fechar(self) -> int:
        mudancas = self.obter_mudancas()
        self.fechar_conexao()
        return mudancas
