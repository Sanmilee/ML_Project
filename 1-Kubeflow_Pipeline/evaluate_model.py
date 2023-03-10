
from kfp.v2 import dsl
from typing import NamedTuple
from kfp.v2.dsl import (Dataset, Input, Metrics, Model, Output)
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
BASE_IMAGE = config['utils']['base_image']

@dsl.component(base_image=BASE_IMAGE, install_kfp_package=False,)
def evaluate_model(
    test_dataset: Input[Dataset], 
    dt_model: Input[Model],
    rf_model: Input[Model],
    metrics: Output[Metrics]
) -> NamedTuple("output", [("optimal_model", str)]):
    
    """Evaluate model on test data"""
    
    import pickle
    import pandas as pd
    import sklearn
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    
    
    def best_model(rf_acc_value, dt_acc_value):
        """get best model base off accuracy"""
        opt_model = "random_forest"
        if dt_acc_value > rf_acc_value:
            opt_model = "decision_tree"
        return opt_model
  

    df = pd.read_csv(test_dataset.path + ".csv")
    X_test = df.iloc[:, :-1]
    y_test = df.iloc[:, -1]
    
     
    # decision tree model evaluation
    decision_tree_train = DecisionTreeClassifier()
    file_name_1 = dt_model.path + ".pkl"
    with open(file_name_1, 'rb') as file:  
        decision_tree_train = pickle.load(file)
    y_pred = decision_tree_train.predict(X_test)
    dt_accuracy = sklearn.metrics.accuracy_score(y_test, y_pred) * 100
    metrics.log_metric("dt_accuracy", round(dt_accuracy, 2))
    
    
    # random forest model evaluation
    random_forest_model = RandomForestClassifier()
    file_name_2 = rf_model.path + ".pkl"
    with open(file_name_2, 'rb') as file:  
        random_forest_model = pickle.load(file)
    y_pred = random_forest_model.predict(X_test)
    rf_accuracy = sklearn.metrics.accuracy_score(y_test, y_pred) * 100
    metrics.log_metric("rf_accuracy", round(rf_accuracy, 2))
    
    
    optimal_model = best_model(rf_accuracy, dt_accuracy)
    return (optimal_model,)
