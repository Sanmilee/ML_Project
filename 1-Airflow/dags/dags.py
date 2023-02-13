# Import packages
import importlib.util
from airflow import DAG
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


# Declare global list for trainable models
CLASSIFIERS = ["KNeighbors_Classifier", "Support_Vector_Machines", "Decision_Tree_Classifier", 
                    "Random_Forest_Classifier", "AdaBoost_Classifier", "Gradient_Boosting_Classifier", 
                    "XGBoost_Classifier", "CatBoost_Classifier"]


def module_from_file(module_name, file_path):
    """
    Function to call python function from another script using importlib

        Parameters:
            module_name (str): mudule name
            file_path (str): file path

        Returns:
            module (funct): callable python function
    """
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# import python module using importlib
foo = module_from_file("main", "/airflow/src/main.py")


# create airflow dag with specifications
with DAG('ml_dag',
        schedule_interval='0 12 * * *',
        start_date=datetime(2017, 3, 20),
        catchup=False) as dag:

    # Dummy task - start
    start_task = DummyOperator(
        task_id='start_task', 
        retries=3)

    # Dummy task - end
    end_task = DummyOperator(
        task_id='end_task', 
        retries=3)


    # load_data task
    load_data = PythonOperator(
        task_id='load_data', 
        python_callable=foo.load_data)

    # best_model task
    best_model = PythonOperator(
        task_id='best_model',
        python_callable=foo.find_optimal_model)

    # dynamic multiple dag execution for training & evaluating models
    for classifier in CLASSIFIERS:
        # training task
        training = PythonOperator(
            task_id='{0}_Model'.format(classifier), 
            python_callable=foo.training,
            op_kwargs={"classifier": classifier})

        # evaluate task
        evaluate = PythonOperator(
            task_id='Evaluate_{0}'.format(classifier),
            python_callable=foo.evaluate, 
            op_kwargs={"classifier": classifier})

        # define dag dependencies
        start_task >> load_data >> training >> evaluate >> best_model >> end_task
    