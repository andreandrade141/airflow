# Airflow Project

## Description

This simulates a data ingest via AirFlow.
The input data is a simple dataset with 6 columns and a few lines.
The objective of this project is to familiarize myself with the ariflow architecture,  DAG declaration and Python usage of Airflow libs.

## Sources

Based on the project present on this site:
<https://www.projectpro.io/article/apache-airflow-data-pipeline-example/610>

## Instalation and Usage

### Requirements

- python 3.7.4 or higher.
- docker
- airflow docker image (can be downloaded here: <https://hub.docker.com/r/apache/airflow>)
- docker-compose plugin

### Instalation

Just `run docker-compose up airflow-init`
After the installation, just run: `docker-compose up` to bring the docker up.
Open the browser and type <http://localhost:8080> to access the AirFlow GUI.
The credencials are default:

- username: airflow
- password: airflow
