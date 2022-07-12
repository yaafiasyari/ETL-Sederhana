#python3


from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from datetime import date
from datetime import datetime
from datetime import timedelta

args = {
    'owner': 'yaafi',
}

dag = DAG(
    dag_id='finalproject_yaafi',
    default_args=args,
    schedule_interval='0 * * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    tags=['finalproject', 'de6']
)

start = DummyOperator(
    task_id='start',
    dag=dag,
) 

postgresql = BashOperator(
    task_id = 'postgresql-db_FinalProject',
    bash_command = 'python3 /home/yaafiasyari/airflow/dags/postgresql_ingest.py',
    dag = dag
)

hadoop = DummyOperator(
    task_id = 'hadoop-datalake',
    dag = dag
)

dwh = BashOperator(
    task_id = 'postgresql-dwh_FinalProject',
    bash_command = 'python3 /home/yaafiasyari/airflow/dags/transform_load.py',
    dag = dag
)

# mart1 = DummyOperator(
#     task_id = 'mart_1',
#     dag = dag
# )

# mart2 = DummyOperator(
#     task_id = 'mart_2',
#     dag = dag
# )

stop = DummyOperator(
    task_id='stop',
    dag=dag,
)
start >>[postgresql] >> hadoop >> dwh >> stop