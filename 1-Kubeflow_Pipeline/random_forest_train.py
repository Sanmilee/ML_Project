
from kfp.v2 import dsl
from kfp.v2.dsl import (Dataset, Input, Model, Output)
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
BASE_IMAGE = config['utils']['base_image']

@dsl.component(base_image=BASE_IMAGE, install_kfp_package=False,)
def random_forest_train(
    train_dataset: Input[Dataset], 
    model: Output[Model]
):
    """Train random_forest model on data, dump model"""
    
    import pickle
    import pandas as pd
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.ensemble import RandomForestClassifier    
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    
    df = pd.read_csv(train_dataset.path + ".csv")
    X_train = df.iloc[:, :-1]
    y_train = df.iloc[:, -1]
    
    # Preprocess features (categorical & numerical)
    # Num features
    numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])
    # Cat features
    categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])
    
    
    # Set target features to preprocess
    numeric_features = X_train.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X_train.select_dtypes(include=['object', 'category']).columns

    # Apply predefined transformations  
    preprocessor = ColumnTransformer(transformers=[
                    ('num', numeric_transformer, numeric_features),
                    ('cat', categorical_transformer, categorical_features)])
    
    
    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    
    
    random_forest_model = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', classifier)])
    random_forest_model.fit(X_train, y_train) 
    
    
    model.metadata["framework"] = "RF"
    file_name = model.path + f".pkl"
    with open(file_name, 'wb') as file:  
        pickle.dump(random_forest_model, file)
        
