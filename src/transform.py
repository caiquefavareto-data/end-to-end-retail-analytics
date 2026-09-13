import pandas as pd
import logging

def clean_data(df):
    logging.info("Transformando e limpando dados...")
    df_clean = df.dropna().copy()
    # Criando a métrica financeira principal
    df_clean['total_amount'] = df_clean['qty'] * df_clean['price']
    return df_clean