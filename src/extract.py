import pandas as pd
import logging

def extract_data():
    logging.info("Extraindo dados legados...")
    # Simulando a extração do arquivo legado de vendas
    data = {
        'transaction_id': [1, 2, 3, 4],
        'date': ['2026-09-01', '2026-09-01', '2026-09-02', '2026-09-02'],
        'store_id': [101, 102, 101, 103],
        'product_id': [501, 502, 501, 503],
        'qty': [2, 1, 3, 1],
        'price': [15.50, 100.0, 15.50, 20.0]
    }
    return pd.DataFrame(data)