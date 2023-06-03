# Import packages
import json
import joblib
import yaml
import pandas as pd
from sklearn.svm import SVC
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier


# Load configuration file specifying inputs
config = yaml.safe_load(open('config.yaml'))

# Declare global variables from config file
DATA_PATH = config['input_data']['training_data']
CLEAN_DATA_PATH = config['input_data']['cleaned_data']
GLOBAL_MODEL_PATH = config['output_path']['model_path']
MODEL_RESULT_SCORE = config['output_path']['model_result_score']


# Dict of trainable models
CLASSIFIER_DICT = {
    "KNeighbors_Classifier": "KNeighborsClassifier(3)",
    "Support_Vector_Machines": 'SVC(kernel="rbf", C=0.025, probability=True)',
    "Decision_Tree_Classifier": "DecisionTreeClassifier()",
    "Random_Forest_Classifier": "RandomForestClassifier()",
    "AdaBoost_Classifier": "AdaBoostClassifier()",
    "Gradient_Boosting_Classifier": "GradientBoostingClassifier()",
    "XGBoost_Classifier": "XGBClassifier()",
    "CatBoost_Classifier": "CatBoostClassifier()"
}


def load_data():
    """
    Loads training data and removes null fields

        Parameters:
            None

        Returns:
            None
    """
    # load data
    df = pd.read_csv(DATA_PATH)
    # drop null fields
    df = df.drop('Time', axis = 1, inplace = True)
    df = df.dropna()
    # save dataframe to csv
    df.to_csv(CLEAN_DATA_PATH, index=False)


def preprocess(classifier):
    """
    Performs preprocessing on training data and feature engineering

        Parameters:
            classifier (model): an ML model definition

        Returns:
            model (model): defined model pipeline
            X_train (dataframe): a pandas datafram for training features
            X_test (dataframe): a pandas datafram for test features
            y_train (dataframe): a pandas datafram for training labels
            y_test (dataframe): a pandas datafram for test labels
    """
    # load data
    df = pd.read_csv(CLEAN_DATA_PATH)
    # split features and labels
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    # split train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # preprocess data schemas
    numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])
    categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])

    numeric_features = list(X_train.select_dtypes(include=['int64', 'float64']).columns)
    categorical_features = list(X_train.select_dtypes(include=['object', 'category']).columns)

    preprocessor = ColumnTransformer(transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)])

    # load model definition
    model_algorithm = eval(CLASSIFIER_DICT[classifier])

    # create model pipeline
    model = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', model_algorithm)])

    return model, X_train, X_test, y_train, y_test


def training(classifier):
    """
    Performs model training on data

        Parameters:
            classifier (model): an ML model pipeline definition

        Returns:
            None
    """
    model, X_train, X_test, y_train, y_test = preprocess(classifier)
    # train model
    model.fit(X_train, y_train)   
    # save trained model
    MODEL_PATH = GLOBAL_MODEL_PATH + f"{classifier}_model.joblib"
    joblib.dump(model, MODEL_PATH)
    print("Training Completed !!")


def evaluate(classifier):
    """
    Performs model evaluation on data

        Parameters:
            classifier (model): an ML model pipeline definition

        Returns:
            None
    """
    # load trained model binary
    model, X_train, X_test, y_train, y_test = preprocess(classifier)
    MODEL_PATH = GLOBAL_MODEL_PATH + f"{classifier}_model.joblib"
    model = joblib.load(MODEL_PATH)
    # evaluate model on test set
    result = model.score(X_test, y_test) * 100
    print(classifier, "score: =====> {:.2f}%".format(result))
    # call function to save model eval result
    save_model_score(classifier, result)
    

def save_model_score(classifier, result): 
    """
    Saves each model evaluation score to a json file during evalustion

        Parameters:
            classifier (model): an ML model pipeline definition
            result (float): model evaluation score

        Returns:
            None
    """
    # Check if file exists, else create new
    if path.isfile(MODEL_RESULT_SCORE) is False:
        print("File not found, creating new file")
        dictionary = {}
        with open(MODEL_RESULT_SCORE, "w") as outfile:
            json.dump(dictionary, outfile)

    # Read and load json file
    with open(MODEL_RESULT_SCORE, 'r') as file:
        json_data = json.load(file)

    # Update result dictionary
    json_data.update({classifier: result})

    # Safe result json
    with open(MODEL_RESULT_SCORE, 'w') as file:
        json.dump(json_data, file, indent=4, separators=(',',': '))
 

def find_optimal_model():
    """
    Search for best evaluation result after evaluation completion

        Parameters:
            None

        Returns:
            best_model (str): model with the best evaluation score
            check (float): value of the higest evaluation score
    """
    
    # Read JSON file
    with open(MODEL_RESULT_SCORE, 'r') as file:
        json_data = json.load(file)

    # get best model from json dict value
    check = 0
    best_model = ''
    for model, score in json_data.items():
        if score > check:
            check = score
            best_model = model
    print("The best model is ====> {} : {:.2f}%".format(best_model, check))
    return best_model, check
