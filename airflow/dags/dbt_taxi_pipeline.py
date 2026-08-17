from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="dbt_taxi_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["dbt", "taxi"],
) as dag:

    dbt_debug = BashOperator(
        task_id="dbt_debug",
        bash_command="""
            cd /opt/airflow/dbt/taxi_analytics &&
            dbt debug --profiles-dir /home/airflow/.dbt
        """,
    )

    dbt_build = BashOperator(
        task_id="dbt_build",
        bash_command="""
            cd /opt/airflow/dbt/taxi_analytics &&
            dbt build --profiles-dir /home/airflow/.dbt
        """,
    )

    dbt_debug >> dbt_build
