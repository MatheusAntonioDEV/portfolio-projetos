```markdown
# Modelagem de Base de Dados e Integração para E-commerce

Projeto focado na estruturação de base de dados relacional e automação de rotinas de inserção e consulta de dados analíticos com Python e SQLite.

## 🚀 Funcionalidades
- Modelagem de tabelas relacionais com aplicação de Chaves Primárias (`PRIMARY KEY`), Chaves Estrangeiras (`FOREIGN KEY`) e regras de integridade referencial.
- Criação e execução automatizada de schema via rotinas Python.
- Carga e inserção de registos em lote.
- Execução de consultas SQL estruturadas (`INNER JOIN`, funções de agregação como `SUM` e `COUNT`, `GROUP BY`) para relatórios analíticos de vendas.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Base de Dados:** SQLite
- **Módulos:** `sqlite3`

## ⚙️ Como Executar
1. Clone este repositório ou descarregue o script de modelagem.
2. No terminal, execute:
   ```bash
   python ecommerce_banco.py

O ficheiro de base de dados SQLite (.db) será criado e as consultas analíticas serão impressas no terminal.
