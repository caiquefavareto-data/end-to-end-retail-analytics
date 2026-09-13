# End-to-End Retail Analytics Pipeline

This project is an automated pipeline that extracts retail data, transforms it, and runs business analytics using SQL.

## 1. Data Engineering (ETL)
* Extracts raw data from legacy systems.
* Cleans and processes data using Python and Pandas.
* Loads the data into a SQLite database using a Star Schema.

## 2. Data Analytics (SQL)
* Connects to the database to run business intelligence queries.
* Uses INNER JOIN and GROUP BY to aggregate revenue.
* Uses HAVING to filter high-performing stores.
* Uses Subqueries to find sales above the global average.

## How to Run
Run the following command in your terminal:
`python src/main.py`
