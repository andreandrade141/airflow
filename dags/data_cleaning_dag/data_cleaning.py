import os
import airflow
import numpy as np
import pandas as pandas

from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

dag_path = os.getcwd()


def data_cleaning() -> None:
    hotel_data = pd.read_csv()
    hotel_data.head()
