# use the official dbt Docker image as a parent image
FROM python:3.10-slim-buster

# setting the working directory to usr/
WORKDIR /usr

COPY models models
COPY tests tests
COPY snapshots snapshots
COPY macros macros
COPY dbt_project.yml dbt_project.yml
COPY Makefile Makefile
COPY profiles.yml profiles.yml
COPY requirements.txt requirements.txt
COPY packages.yml packages.yml
COPY dbt_run.py /usr/python/

RUN pip install --upgrade pip
RUN pip install dbt-databricks

RUN dbt deps

CMD ["python", "/usr/python/dbt_run.py"]



