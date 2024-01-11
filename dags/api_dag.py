import json
from datetime import datetime
from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor           # An Airflow sensor to monitor HTTP endpoints.
from airflow.providers.http.operators.http import SimpleHttpOperator # An Airflow operator for making HTTP requests.
from airflow.operators.python import PythonOperator


with DAG(
    dag_id='api_dag',
    schedule = '@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False                         # Ensures that the DAG doesn't backfill or catch up with any missing scheduled intervals.

) as dag:

    task_is_api_active = HttpSensor(
        task_id='is_api_active',
        http_conn_id='api_posts',
        endpoint='posts/'
    )                                              
            # This workflow monitors the availability of an API endpoint and retrieves posts from that endpoint using HTTP requests within an Apache Airflow DAG.

    task_get_posts = SimpleHttpOperator(
        task_id='get_posts',
        http_conn_id='api_posts',
        endpoint = 'posts/',
        method= 'GET',
        response_filter = lambda response: json.loads(response.text),  # A lambda function to process the HTTP response by converting it from JSON to a Python object using json.loads(response.text)
        log_response = True
    )
