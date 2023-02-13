## MLOps Projects
- Displaying practices, tools and implementation that aims to deploy and maintain machine learning models in production reliably and efficiently. 
***


### Table of Contents
***
1. [Project Overview](#1.-project-overview)
2. [Airflow & Cloud Composer](#airflow-&-cloud-composer)
3. [TFX](#tfx)
4. [Kubeflow Pipeles with GCP Vertex AI](#kubeflow-pipeles-with-gcp-vertex-ai)

***
### 1. Project Overview

This project focuses on streamlining the machine learning model development process by implementing MLOps best practices and tools. The goal is to ensure that models are developed in a sustainable, scalable, and repeatable manner. The project is defined as config-based.

- Three projects are described here with diffrent ML orchestrating and pipline tools/platform (Airflow, TFX and Vertex AI)
***

### Airflow & Cloud Composer
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
### TFX
- Intro
- Infrastructure
- Tools and Technologies
- Usage

***
### Kubeflow Pipeles with GCP Vertex AI
- Intro
- Infrastructure
- Tools and Technologies
- Usage


### 1. Task

`Pet Adoption Classifier`
- This is a supervised model which trains an XGBoost Model to predict if a pet would be adopted or not.


### 2. Data

Contains 13 features and a labeled column (Yes or No) if a pet can be adopted. `gs://cloud-samples-data/ai-platform-unified/datasets/tabular/petfinder-tabular-classification.csv`

### 3. Requirements

- gcsfs==2022.1.0
- numpy==1.19.5
- pandas==1.3.5
- scikit-learn==1.0.1
- xgboost==1.5.1
- Python==3.8.0
- matplotlib==3.5.1



### 4. Files
This directory contains 3 python 3 scripts
- `train.py`: Script to build and train a XGBoost classifier on the petFinder data (to run – python train.py)
- `predictor.py`: Script to test the saved XGBoost classifier on the whole data (to run – python predictor.py
- `test_predictor`: Unit Test script to automate testing of the model prediction function (to run – python predictor.py)


- - The directory also contains all the above script in 2 jupyter notebooks.


