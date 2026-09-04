from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime

with DAG(
    dag_id="grocery_sales_databricks_pipeline",
    start_date=datetime(2026, 9, 1),
    schedule=None,
    catchup=False,
    tags=["grocery-sales", "databricks"],
) as dag:

    trigger_databricks_job = DatabricksRunNowOperator(
        task_id="trigger_grocery_sales_job",
        databricks_conn_id="databricks_default",
        job_id=357532297946035
    )
