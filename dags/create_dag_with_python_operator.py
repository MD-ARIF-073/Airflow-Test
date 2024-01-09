from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'arif',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# def greet(name, age):
#     print(f"Hello World! My name is {name}, "
#           f"and I am {age} years old!")
    
# def greet(ti):
#     name = ti.xcom_pull(task_ids='get_name')
#     print(f"Hello World! My name is {name}, "
#           f"and I am {age} years old!") 
    
def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello World! My name is {first_name} {last_name}, "
          f"and I am {age} years old!")         


# def get_name():
#     return 'SANI'


def get_name(ti):
    ti.xcom_push(key='first_name', value='Arif')
    ti.xcom_push(key='last_name', value='Ishtiaq')

def get_age(ti):
    ti.xcom_push(key='age', value=25)    



with DAG(
    dag_id='our_first_dag_with_python_operator_v06',
    default_args=default_args,
    description='This is my first dag using python operator',
    start_date=datetime(2024, 1, 8),  # Use datetime object
    schedule_interval='@daily'  # Corrected parameter name
) as dag:
    task1 = PythonOperator(
        task_id = 'greet',
        python_callable=greet,
       # op_kwargs={'age' : 25}                       # parameter op_kwargs is a dictionary arguments that will get unopacked in the python function
    )

    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable=get_name

    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    # task2 >> task1              # task1 is the downstream of task2

    [task2, task3] >> task1     # task3 and task2 are the upstream of task1
 
   # task1