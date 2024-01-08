from datetime import datetime, timedelta
from airflow import DAG   
from airflow.operators.bash_operator import BashOperator  # Updated import statement

default_args = {
    'owner': 'arif',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This is my first dag',
    start_date=datetime(2024, 1, 8, 5),  # Use datetime object
    schedule_interval='@daily'  # Corrected parameter name
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world! This is apache airflow talking to you"
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = "echo hey, I am task2 and will be running after the task1!"
    )

    task3 = BashOperator(
        task_id = 'third_task',
        bash_command = "echo hey, I am task3 and will be running after task1 and with the same time as task2"
    )


    # Task dependency method 1
    #task1.set_downstream(task2)              # This is where you'd define additional tasks and their dependencies if needed
    #task1.set_downstream(task3)

    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3


    # Task dependency method 3

    task1 >> [task2, task3]
