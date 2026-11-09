import sqlite3

# 1. Conecta ao banco de dados (se o arquivo não existir, ele cria na hora)
conexao = sqlite3.connect("ecommerce.db")
cursor = conexao.cursor()

print("Criando as tabelas do E-commerce...")

# 2. Criação da tabela de Clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    data_cadastro TEXT
);
""")

# 3. Criação da tabela de Produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
    id_produto INTEGER PRIMARY KEY,
    nome_produto TEXT NOT NULL,
    preco REAL,
    estoque INTEGER
);
""")

# 4. Criação da tabela de Pedidos (Relacionando as duas)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Pedidos (
    id_pedido INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_produto INTEGER,
    data_pedido TEXT,
    quantidade INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);
""")

# 5. Inserindo dados de teste para ver o negócio funcionando
# Limpa os dados anteriores para não duplicar se rodar duas vezes
cursor.execute("DELETE FROM Pedidos")
cursor.execute("DELETE FROM Clientes")
cursor.execute("DELETE FROM Produtos")

cursor.execute("INSERT INTO Clientes VALUES (1, 'Matheus Antonio', 'matheus@email.com', '2026-11-08')")
cursor.execute("INSERT INTO Clientes VALUES (2, 'Ana Costa', 'ana@email.com', '2026-11-07')")

cursor.execute("INSERT INTO Produtos VALUES (101, 'Teclado Mecânico', 250.00, 15)")
cursor.execute("INSERT INTO Produtos VALUES (102, 'Mouse Gamer', 150.00, 30)")

cursor.execute("INSERT INTO Pedidos VALUES (501, 1, 101, '2026-11-08', 1)") # Matheus comprou 1 teclado
cursor.execute("INSERT INTO Pedidos VALUES (502, 2, 102, '2026-11-08', 2)") # Ana comprou 2 mouses

conexao.commit()
print("Tabelas criadas e dados inseridos com sucesso!\n")

# 6. Executando a Consulta Relacional (INNER JOIN) para gerar o relatório
print("--- RELATÓRIO DE VENDAS (INNER JOIN) ---")
consulta_join = """
SELECT 
    c.nome AS Nome_Cliente,
    p.nome_produto AS Produto,
    pe.quantidade AS Qtd,
    (pe.quantidade * p.preco) AS Total_Pago
FROM Pedidos pe
INNER JOIN Clientes c ON pe.id_cliente = c.id_cliente
INNER JOIN Produtos p ON pe.id_produto = p.id_produto;
"""

cursor.execute(consulta_join)
resultados = cursor.fetchall()

# Exibe o resultado formatado na tela
for linha in resultados:
    print(f"Cliente: {linha[0]} | Produto: {linha[1]} | Qtd: {linha[2]} | Total: R$ {linha[3]:.2f}")

# Fecha a conexão
conexao.close()
