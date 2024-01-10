import json
from datetime import datetime
from airflow import DAG
from airflow.models import dag
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator



with DAG(
    dag_id='api_dag',
    schedule = '@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False

) as dag:
    

    task_is_api_active = HttpSensor(
        task_id='is_api_active',
        http_conn_id='api_posts',
        endpoint='posts/'
    )

    task_get_posts = SimpleHttpOperator(
        task_id='get_posts',
        http_conn_id='api_posts',
        endpoint = 'posts/',
        method= 'GET',
        response_filter = lambda response: json.loads(response.text),
        log_response = True
    )