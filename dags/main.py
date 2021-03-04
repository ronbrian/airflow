"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.postgres_operator import PostgresOperator


default_args = {
    'owner': 'interintel',    
    'start_date': datetime(2018, 3, 1),
    # 'end_date': datetime(2018, 12, 30),
    'depends_on_past': False,
    'email': ['brian.machoka@interintel.co.ke'],
    'email_on_failure': False,
    'email_on_retry': False,
    # If a task fails, retry it once after waiting
    # at least 5 minutes
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    }

dag = DAG(
    'PostgreSQLBackup',
    default_args=default_args,
    description='Dag to backup postgres Database daily',
    # Continue to run DAG once per day
    # schedule_interval=timedelta(days=1),
)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = PostgresOperator(
        task_id='test_db_connection',
        sql='''  SELECT datname FROM pg_database WHERE datistemplate = false;  ''',
        dag=dag,
    )

t2 = BashOperator(
    task_id='confirm_storage_mount',
    depends_on_past=False,
    bash_command='echo "works" ',
    dag=dag,
)

# templated_command = """
# {% for i in range(5) %}
#     echo "{{ ds }}"
#     echo "{{ macros.ds_add(ds, 7)}}"
#     echo "{{ params.my_param }}"
# {% endfor %}
# """

# t3 = BashOperator(
#     task_id='templated',
#     depends_on_past=False,
#     bash_command=templated_command,
#     params={'my_param': 'Parameter I passed in'},
#     dag=dag,
# )

t3 = BashOperator(
    task_id='backup_commands',
    depends_on_past=False,
    bash_command='echo "works" ',
    dag=dag,
)

t4 = BashOperator(
    task_id='locate_dump_file',
    depends_on_past=False,
    bash_command='echo "works" ',
    dag=dag,
)

t5 = BashOperator(
    task_id='rename_dump_file',
    depends_on_past=False,
    bash_command='echo "works" ',
    dag=dag,
)

t6 = BashOperator(
    task_id='copy_dump_file',
    depends_on_past=False,
    bash_command='echo "works" ',
    dag=dag,
)

t7 = BashOperator(
    task_id='delete_previousdays_records',
    depends_on_past=False,
    bash_command='echo "works" ',
    dag=dag,
)

# t7 = BashOperator(
#     task_id='delete_previousdays_records',
#     depends_on_past=False,
#     bash_command='echo "works" ',
#     dag=dag,
# )



#Setting Up Dependencies

# This means that t2 will depend on t1
# running successfully to run.
t1.set_downstream(t3)


# similar to above where t3 will depend on t1
t3.set_upstream(t2)
t3.set_downstream(t4)
t4.set_downstream(t5)
t3.set_downstream(t4)

# The bit shift operator can also be
# used to chain operations:
# t1 >> t2

# And the upstream dependency with the
# bit shift operator:
# t2 << t1


# A list of tasks can also be set as
# dependencies. These operations
# all have the same effect:

# t1.set_downstream([t2, t3])
# t1 >> [t2, t3]
# [t2, t3] << t1