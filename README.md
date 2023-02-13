## MLOps Projects
- Displaying practices, tools and implementation that aims to deploy and maintain machine learning models in production reliably and efficiently. 
***


### Table of Contents
***
1. [Project Overview](#1-project-overview)
2. [Airflow & Cloud Composer](#airflow-&-cloud-composer)
3. [TFX](#tfx)
4. [Kubeflow Pipeles with GCP Vertex AI](#kubeflow-pipeles-with-gcp-vertex-ai)

***
### 1 Project Overview

This project focuses on streamlining the machine learning model development process by implementing MLOps best practices and tools. The goal is to ensure that models are developed in a sustainable, scalable, and repeatable manner. The project is defined as config-based.

- Three projects are described here with diffrent ML orchestrating and pipline tools/platform (Airflow, TFX and Vertex AI)
***

### 2. Airflow & Cloud Composer
#### Intro
This project aims to demonstrate the use of Apache Airflow and Google Cloud Composer for orchestrating machine learning workflows. The goal is to showcase the benefits of using a workflow management system for managing the end-to-end lifecycle of machine learning models. The project will cover tasks such as data inception, processing, feature engineering, model training, and evaluation - which could then be deployed.



#### Infrastructure
The project consists of the 3 folders
- Dags: Conataining the airflow tasks, where each task is defined as dags performed in a sequential manner, with the output of one task serving as the input to the next.
- Script: A folder containing python logic where the defined tasks are written for data loading ang processing, Feature Engineering, Model Training and evaluation
Data: where the training data is located



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
The entire workflow will be automated using Apache Airflow and Google Cloud Composer. This will involve defining the workflow as a series of tasks, and configuring each task to run automatically in response to specific events or conditions. To take advantage of scalbility in the cloud, the dags are defined in associated GCS buckets and excuted in composer airflow automatically. The running dags can be viewed in the airflow web UI page.
































***
### 3. TFX
- Intro
- Infrastructure
- Tools and Technologies
- Usage

***
### 4. Kubeflow Pipeles with GCP Vertex AI
- Intro
- Infrastructure
- Tools and Technologies
- Usage



- - The directory also contains all the above script in 2 jupyter notebooks.


