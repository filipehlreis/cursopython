import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def fechar(self):
        self.cursor.close()
        self.conn.close()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Luiz', '111111')
    # agenda.inserir('Maria', '222222')
    # agenda.inserir('Joao', '333333')
    # agenda.inserir('Rose', '444444')
    # agenda.inserir('Guilherme', '555555')
    # agenda.inserir('Fabricio', '666666')
    # agenda.editar('Francisco', 131313, 10)
    # agenda.excluir(10)

    # agenda.inserir('Luiz Otavio', 102321)
    # agenda.inserir('Luiz Felipe', 102322)
    # agenda.inserir('Ronaldo Luiz', 102323)
    # agenda.inserir('R. Luiza', 102324)
    # agenda.inserir('R. Luiza meio do caminho', 102325)

    agenda.buscar('luiz')
