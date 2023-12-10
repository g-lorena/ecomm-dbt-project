from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

# Define your Airflow DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 1),
    'retries': 1,
}

dag = DAG('run_main_py_in_ecr_container', default_args=default_args, schedule_interval='@daily')

# Define the task to run main.py using DockerOperator
run_main_py = DockerOperator(
    task_id='run_main_py_in_ecr_container',
    image='957951454565.dkr.ecr.eu-west-3.amazonaws.com/ecomm-dbt-project:1.0.1',  # Replace with your ECR image and tag
    command='python /usr/python/dbt_run.py',  # Command to execute main.py within the container
    docker_conn_id='docker',
    api_version='auto',
    network_mode="bridge",
    dag=dag,
)

run_main_py
