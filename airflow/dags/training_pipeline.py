from asyncio import tasks
import json
from textwrap import dedent
import pendulum
import os

##The DAG OBJECT ; WE LL NEED THIS TO INSTANTIATE a DAG
##DIRECTED ACYCLIC GRAPH
from airflow import DAG 
#
training_pipeline=None

#operators ; we need to operate
from airflow.operators.python  import PythonOperator

#  [END importETL DAG tutorial_prediction',
#       #[START default_args]
# #These args will get passed on to each operator
# #you can override them on a per-task basis during operator initilaization

with DAG(
    'sensor_training',
    default_args={'retries':2},
    #[END default_args]
    description = 'Sensor Fault Dection',
    schedule_interval="@weekly",
    start_date=pendulum.datatime(2022, 12, 11,tz="UTC"),
    catchup=False,
    tags=['example'],

) as dags:

# #   [END instantiate_dag]
# #   [START documentation]
#     dag.doc_md=__doc__
#     #[END documentation]

    
    def training(**kwargs):
        from sensor.pipeline.training_pipeline import start_training_pipeline
        start_training_pipeline()

    def sync_artifact_to_s3_bucket(**kwargs):
        bucket_name=os.getenv("BUCKET_NAME")
        os.system(f"aws s3 sync /app/artifact s3://{bucket_name}/artifacts")
        os.system(f"aws s3 sync /app/saved_models s3://{bucket_name}/saved_models")

    training_pipeline = PythonOperator(
            task_id="train_pipeline",
            python_callable=training
    )

    sync_data_to_s3=PythonOperator(
            task_id="sync_data_to_s3",
            python_callable=sync_artifact_to_s3_bucket
    )



    training_pipeline >> sync_data_to_s3

