
from kfp.v2 import dsl
from kfp.v2.dsl import (Dataset, Input, Output)
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
BASE_IMAGE = config['utils']['base_image']

@dsl.component(base_image=BASE_IMAGE, install_kfp_package=False,)
def preprocessing(
    dataset: Input[Dataset], 
    train_dataset: Output[Dataset],
    test_dataset: Output[Dataset]
):
    """Preprocess data"""
    
    import pandas as pd
    from sklearn.model_selection import train_test_split

    df = pd.read_csv(dataset.path + ".csv")
    df = df.dropna()
    
    train_data, test_data = train_test_split(df)
    
    train_data.to_csv(train_dataset.path + ".csv", index=False)
    test_data.to_csv(test_dataset.path + ".csv", index=False)
    
