import sqlite3
import pandas as pd
import logging

def run_business_analytics():
    logging.info("Iniciando motor de Analytics (SQL Avançado)...")
    conn = sqlite3.connect('retail_dw.db')
    cursor = conn.cursor()

    # DDL e DML: Garantindo que as dimensões existam no ecossistema
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS Dim_Product (
        product_id INTEGER PRIMARY KEY,
        category VARCHAR(50)
    );
    CREATE TABLE IF NOT EXISTS Dim_Store (
        store_id INTEGER PRIMARY KEY,
        store_name VARCHAR(50)
    );
    INSERT OR IGNORE INTO Dim_Product (product_id, category) VALUES (501, 'Eletrônicos'), (502, 'Roupas'), (503, 'Acessórios');
    INSERT OR IGNORE INTO Dim_Store (store_id, store_name) VALUES (101, 'Loja Matriz'), (102, 'Loja Shopping'), (103, 'Loja Sul');
    ''')
    conn.commit()

    # Consulta 1: Performance por Categoria (JOIN e Agregação)
    query_cat = '''
    SELECT p.category AS Categoria, SUM(f.total_amount) AS Faturamento_Total
    FROM Fact_Sales f
    INNER JOIN Dim_Product p ON f.product_id = p.product_id
    GROUP BY p.category ORDER BY Faturamento_Total DESC;
    '''
    print("\n--- PERFORMANCE POR CATEGORIA ---")
    print(pd.read_sql_query(query_cat, conn))

    # Consulta 2: Lojas de Alta Performance (HAVING)
    query_having = '''
    SELECT s.store_name AS Loja, SUM(f.total_amount) AS Faturamento
    FROM Fact_Sales f
    INNER JOIN Dim_Store s ON f.store_id = s.store_id
    GROUP BY s.store_name HAVING SUM(f.total_amount) > 50;
    '''
    print("\n--- LOJAS ALTA PERFORMANCE (HAVING > 50) ---")
    print(pd.read_sql_query(query_having, conn))

    # Consulta 3: Vendas Acima da Média (Subconsulta)
    query_sub = '''
    SELECT transaction_id AS Transacao, total_amount AS Valor
    FROM Fact_Sales
    WHERE total_amount > (SELECT AVG(total_amount) FROM Fact_Sales);
    '''
    print("\n--- VENDAS ACIMA DA MÉDIA (SUBCONSULTA) ---")
    print(pd.read_sql_query(query_sub, conn))

    conn.close()