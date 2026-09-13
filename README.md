# End-to-End Retail Analytics Pipeline

An enterprise-grade, integrated data ecosystem designed to automate the complete lifecycle of retail data—from raw legacy extraction to advanced SQL business intelligence. This master orchestrator unifies **Data Engineering** and **Data Analytics** into a single, automated end-to-end pipeline.

---

## Architecture Overview

The pipeline operates in two modular, fully automated phases:

```text
[ Legacy Data ] ──> ( 1. Extract ) ──> ( 2. Clean/Transform ) ──> [ SQLite Data Warehouse ]
                                                                             │
[ Strategic Metrics ] <── ( 4. SQL Analytics Engine ) <── ( 3. Star Schema ) ┘

Detailed Pipeline Phases
Phase 1: Automated ETL Pipeline (Data Engineering)
Extraction: Dynamically ingests raw transaction data from legacy file structures.

Transformation: Cleanses missing values, sanitizes record types, and calculates total transaction values using Python and Pandas.

Loading: Structures cleaned data into a local SQLite Data Warehouse following a robust Star Schema dimensional architecture.

Phase 2: Advanced SQL Business Analytics (Data Analytics)
Once the Data Warehouse is updated, the analytics engine executes complex SQL queries to deliver business intelligence:

Category Performance: Aggregates revenue using INNER JOIN across Dimension and Fact tables with GROUP BY.

High-Performance Filtering: Filters aggregated metrics post-calculation using the HAVING clause to highlight top-performing stores.

Dynamic Benchmarking: Leverages nested Subqueries in the WHERE clause to dynamically identify sales exceeding global averages.

Technical Stack & Concepts Applied
Languages: Python 3.x, SQL (SQLite dialect)

Libraries: Pandas, SQLite3, Logging

Data Modeling: Star Schema (Fact_Sales, Dim_Product, Dim_Store)

SQL Techniques: Multi-table JOINs, Aggregations (SUM, AVG), GROUP BY, HAVING, Nested Subqueries

Software Design: Modular architecture, automated pipeline orchestration, environment logging

Repository Structure
Plaintext
end-to-end-retail-analytics/
├── src/
│   ├── extract.py         # Legacy data extraction module
│   ├── transform.py       # Data cleansing & transformation engine
│   ├── load.py            # Star Schema DW loader
│   ├── analytics.py       # Advanced SQL analytics engine
│   └── main.py            # Master pipeline orchestrator
├── data/                  # Raw input datasets
├── retail_dw.db           # SQLite Data Warehouse instance
├── README.md              # Project documentation
└── .gitignore             # Git exclusion rules