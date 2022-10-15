import os
import airflow
import numpy as np
import pandas as pandas

from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

dag_path = os.getcwd()


def data_cleaning() -> None:
    '''
        This method cleans up all empty cells, adding some placeholder value.

    '''
    hotel_data = pd.read_csv("raw_data/raw.csv")
    hotel_data.head()
    hotel_data.info()
    hotel_data.describe()

    hotel_data.isnull().sum()

    nan_replacements = {"children": 0,
                        "country": "Unknown", "agent": "Organic Booking", "company": "Personal Booking"}

    cleaned_data = hotel_data.fillna(nan_replacements)

    cleaned_data.info()

    cleaned_data.to_csv("processed_data/output.csv", index=False)


def cleaned_data_message() -> None:
    print("Data succesfully cleaned")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": airflow.utils.dates.days_ago(7)
}

data_cleaning_dag = DAG(
    'data_cleaning',
    default_args=default_args,
    schedule_interval=timedelta(days=30),
    catchup=False
)

clean_data = PythonOperator(
    task_id="data_cleaning",
    python_callable=cleaned_data_message,
    dag=data_cleaning_dag,
)

message = PythonOperator(
    task_id="cleaned_data_message",
    python_callable=cleaned_data_message,
    dag=data_cleaning_dag
)

clean_data >> message
