from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'arif',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_cron_expression_v04',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),  # Use datetime object
    schedule='0 4 * * Wed-Fri'  #  airflow cron preset
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command="echo dag with cron expression!"
    )


    task1
