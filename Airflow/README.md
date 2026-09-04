# Airflow Orchestration

Apache Airflow is used to orchestrate the existing Databricks ETL pipeline.

## Pipeline Flow

Airflow DAG → Databricks Job → Silver → Gold → PyTest → Slack
