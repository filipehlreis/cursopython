import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#                {'nome': 'Joaozinho', 'peso': 25})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'Daniel', 'peso': 123})
# conexao.commit()


# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
#                {'nome': 'Joana', 'id': 2}
#                )

# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {'id': 2}
# )


# conexao.commit()

# cursor.execute('SELECT * FROM clientes')

cursor.execute(
    'SELECT nome, peso FROM clientes WHERE peso > :peso',
    {'peso': 50}
)

for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)

cursor.close()
conexao.close()
