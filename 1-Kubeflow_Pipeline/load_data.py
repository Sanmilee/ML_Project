
from kfp.v2 import dsl
from kfp.v2.dsl import (Dataset, Output)
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
BASE_IMAGE = config['utils']['base_image']

@dsl.component(base_image=BASE_IMAGE, install_kfp_package=False,)
def load_data(
    bq_table: str, 
    output_data_path: Output[Dataset]
):
    """Pull conversion data from bigquery and dump to csv in gcs"""

    import os
    import pandas as pd
    from google.cloud import bigquery

    project_number = os.environ["CLOUD_ML_PROJECT_ID"]
    bqclient = bigquery.Client(project=project_number)
    table = bigquery.TableReference.from_string(bq_table)
    rows = bqclient.list_rows(table)
    dataframe = rows.to_dataframe(create_bqstorage_client=True)
    dataframe = dataframe.sample(frac=1, random_state=2)
    dataframe.to_csv(output_data_path.path + ".csv", index=False)
    
