## MLOps Projects
- Displaying practices, tools and implementation that aims to deploy and maintain machine learning models in production reliably and efficiently. 
***


### Table of Contents
***
1. [Project Overview](#1-project-overview)
2. [Kubeflow Pipelines with GCP Vertex AI](#2-kubeflow-pipelines-with-gcp-vertex-ai)
3. [Airflow & Cloud Composer](#3-airflow-and-cloud-composer)
4. [TFX End-to-end ML Pipeline](#4-tfx-end-to-end-ml-pipeline)

***
### 1 Project Overview

This project focuses on streamlining the machine learning model development process by implementing MLOps best practices and tools. The goal is to ensure that models are developed in a sustainable, scalable, and repeatable manner. The project is defined as config-based.

- Three projects are described here with diffrent ML orchestrating and pipline tools/platform (Airflow, TFX and Vertex AI)

***
### 2 Kubeflow Pipelines with GCP Vertex AI
#### Intro
This project demonstrate the use of Kubeflow Pipelines and Google Cloud Vertex AI to simplify the entire ML workflow to build, train, deploy and serve ML models in a distributed manner. The goal is to showcase the benefits of using these tools for managing the end-to-end lifecycle of machine learning models. The project will cover the automation of tasks such as data processing, feature engineering, model training, deployment, and monitoring.

#### Infrastructure
The project consists of a jupyter notebook with 5 vertex components to:
- load data
- preprocess data
- train models
- evaluate model
- deploy models

#### Tools and Technologies
The following tools and technologies will be used in this project:
- Kubeflow Pipelines
- Google Cloud Vertex AI
- TensorFlow
- Google Cloud Storage
- Google Cloud AI Platform
- TensorBoard

#### Usage
- Run the jupyter notebook with the right config variables to test run

***
### 3 Airflow and Cloud Composer
#### Intro
This project demonstrate the use of Apache Airflow and Google Cloud Composer for orchestrating machine learning workflows. This will involve defining the workflow as a series of tasks, and configuring each task to run automatically in response to specific events or conditions. The goal is to showcase the benefits of using a workflow management system for managing the end-to-end lifecycle of machine learning models. The project will cover tasks such as data inception, processing, feature engineering, model training, and evaluation - which could then be deployed.

#### Infrastructure
The project consists of the 3 folders
- Dags: Conataining the airflow tasks, where each task is defined as dags performed in a sequential manner, with the output of one task serving as the input to the next.
- Script: A folder containing python logic where the defined tasks are written for data loading and processing, Feature Engineering, Model Training and evaluation
- Data: where the training data is located

#### Tools and Technologies
The following tools and technologies will be used in this project:
- Apache Airflow
- Google Cloud Composer
- Google Cloud Storage
- TensorFlow
- Scikit-learn
- Pandas
- Yaml

#### Usage
The entire workflow will be automated using Apache Airflow and Google Cloud Composer. To take advantage of scalability in the cloud, the dags are defined in associated GCS buckets and excuted in composer airflow automatically. The running dags can be viewed in the airflow web UI page.

<!-- ![images1](2-Airflow/images/dag_img_2.png) -->

***
### 4 TFX End-to-end ML Pipeline
#### Intro
This project demonstrate the use of TensorFlow Extended (TFX) for orchestrating machine learning workflows. The goal is to showcase the benefits of using TFX for managing the end-to-end lifecycle of machine learning models.


#### Infrastructure

The project utilizes all of TFX' components for data loading, processing, Feature Engineering, Model Training, evaluation, deployment, monitoring and validation. By automating the entire lifecycle of machine learning models, the project will showcase the efficiency and scalability gains that can be achieved through the use of TFX.


#### Tools and Technologies
The following tools and technologies will be used in this project:
- TensorFlow Extended (TFX)
- TensorFlow
- Apache Beam
- TensorBoard

#### Usage
The project is executed by running the main script via `python main.py` 
