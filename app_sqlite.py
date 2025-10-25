"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""


import sqlite3

conn= sqlite3.connect("escola.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT                                            
               )''')

print("Tabela criada com sucesso!\n")

cursor.execute("INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)",("Richard", 23, "richard@gmail.com"))
cursor.execute("INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)",("Rebeca", 29, "beccare@gmail.com"))
cursor.execute("INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)",("Ismael", 27, "ismael45@gmail.com"))
cursor.execute("INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)",("Gabriella", 22, "gabii@gmail.com"))

conn.commit()
print("Itens adicionados à lista.\n")

print("Listar de alunos cadastrados:")
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)
print() 

cursor.execute("UPDATE alunos SET email = ? WHERE id = ?",("becca57@gmail.com", "2"))

conn.commit()
print('Após atualização do email da Rebeca:')
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)
print()

cursor.execute("DELETE FROM  alunos WHERE id= ?",(2,))
conn.commit()
print('Após deletar o id 2:')
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)
print()

conn.close()
