FROM python:3.7-slim-buster

RUN mkdir /mnt/mlruns/
RUN chmod 777 -R /mnt/mlruns/

# Install python packages
RUN pip install mlflow boto3 pymysql


# ENTRYPOINT mlflow server --host 0.0.0.0 --backend-store-uri mysql+pymysql://admin:admin@db:3306/mlflow_db --default-artifact-root  file://mnt/mlruns/  
