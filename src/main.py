import logging
from extract import extract_data
from transform import clean_data
from load import load_to_dw
from analytics import run_business_analytics

def run_integrated_pipeline():
    logging.info("--- INICIANDO FASE 1: PIPELINE ETL ---")
    raw_data = extract_data()
    processed_data = clean_data(raw_data)
    load_to_dw(processed_data)
    logging.info("ETL concluído com sucesso. Data Warehouse atualizado.")
    
    logging.info("--- INICIANDO FASE 2: SQL DATA ANALYTICS ---")
    run_business_analytics()
    
    logging.info("--- PIPELINE END-TO-END FINALIZADO ---")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    run_integrated_pipeline()