"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.postgres_operator import PostgresOperator



default_args = {
    "owner": "interintel",
    "depends_on_past": False,
    "start_date": datetime(2021, 3, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    'schedule_interval': None
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag_params = {
    'dag_id': 'PostgresOperator_dag',
    'start_date': datetime(2021, 3, 1),
    'schedule_interval': None
}

with DAG(**dag_params) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        sql='''CREATE TABLE new_table(
            custom_id integer NOT NULL, timestamp TIMESTAMP NOT NULL, user_id VARCHAR (50) NOT NULL
            );''',
    )

with DAG(**dag_params) as dag:

    create_table = PostgresOperator(
        task_id='show_all_databases',
        sql='''  SELECT datname FROM pg_database WHERE datistemplate = false;  ''',
    )