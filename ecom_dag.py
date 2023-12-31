from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.bash_operator import BashOperator

# Define your Airflow DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG('run_main_py_in_ecr_container', default_args=default_args, schedule="40 5 16 * *")

''' 
def print_hello():
    print("Hello, MWAA!")

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag
)
'''

# Define the task to run main.py using DockerOperator

run_main_py = DockerOperator(
    task_id='pull_hello_world',
    image='hello-world',  # Docker Hub image name
    api_version='auto',   # Use Docker API version automatically detected
    auto_remove=True,     # Remove the container after execution
    command='echo Hello from Docker!',  # Command to be executed in the container
    dag=dag
)

run_main_py

# Define the task dependency
#hello_task
