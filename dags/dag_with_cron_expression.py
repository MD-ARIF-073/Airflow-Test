from datetime import datetime, timedelta         # Imports the datetime and timedelta classes from the datetime module, used for working with dates and time intervals.
from airflow import DAG                          # Imports the DAG class from the airflow module, which is the core concept for defining workflows in Apache Airflow.
from airflow.operators.bash import BashOperator  # 


default_args = {                                 # Defines a dictionary called default_args to set common arguments that will be applied to all tasks in the DAG
    'owner': 'arif',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

# Creates a new DAG object with the following configuration
with DAG(
    dag_id='dag_with_cron_expression_v06',       
    default_args=default_args,
    start_date=datetime(2024, 1, 11),  # Use datetime object
    schedule='1 * * * *'  #  airflow cron preset, sets a cron expression for the DAG to run every minute (at the beginning of each minute).
) as dag:
    task1 = BashOperator(
        task_id = 'task1',                   # a unique identifier to the task.
        bash_command="echo hello world! This is Arif Ishtiaq talking to apache airflow!"
    )


    task1                         # ensures that the task is included in the workflow.



