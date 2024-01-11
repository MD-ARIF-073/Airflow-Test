from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def print_hello():
    print("Hello World")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple DAG that prints Hello World every 10 seconds',
    schedule=timedelta(seconds=10),
)

task_hello_world = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)
