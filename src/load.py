import sqlite3
import logging

def load_to_dw(df):
    logging.info("Carregando dados na tabela Fato (Data Warehouse)...")
    conn = sqlite3.connect('retail_dw.db')
    # Substitui a tabela fato a cada execução para manter os testes limpos
    df.to_sql('Fact_Sales', conn, if_exists='replace', index=False)
    conn.close()