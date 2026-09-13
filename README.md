# End-to-End Retail Analytics Pipeline

An enterprise-grade, integrated data ecosystem designed to automate the complete lifecycle of retail data—from raw legacy extraction to advanced SQL business intelligence. This master orchestrator unifies **Data Engineering** and **Data Analytics** into a single, automated end-to-end pipeline.

---

## Architecture Overview

The pipeline operates in two modular, fully automated phases:

```text
[ Legacy Data ] ──> ( 1. Extract ) ──> ( 2. Clean/Transform ) ──> [ SQLite Data Warehouse ]
                                                                             │
[ Strategic Metrics ] <── ( 4. SQL Analytics Engine ) <── ( 3. Star Schema ) ┘