
from kfp.v2 import dsl
from typing import NamedTuple
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
BASE_IMAGE = config['utils']['base_image']

@dsl.component(base_image=BASE_IMAGE, install_kfp_package=False,)
def deploy_model(
    model: Input[Model],
    project: str,
    region: str,
    container_image : str, 
    vertex_endpoint: Output[Artifact],
    vertex_model: Output[Model] 
):
    """Train sklearn model on bean data csv, dump model"""
    
    from google.cloud import aiplatform
    aiplatform.init(project=project, location=region)
    
    
    DISPLAY_NAME  = "conversion_model"
    MODEL_NAME = "conversion_model_v1"
    ENDPOINT_NAME = "conversion_endpoint"
    
    
    # Create vertex endpoint
    endpoint = aiplatform.Endpoint.create(
        display_name=ENDPOINT_NAME, 
        project=project, 
        location=region
    )
    
    
    # Upload model to vertex model registry
    model_upload = aiplatform.Model.upload(
        display_name = DISPLAY_NAME, 
        artifact_uri = model.uri.replace("model", ""),
        serving_container_image_uri =  container_image,
        serving_container_health_route=f"/v1/models/{MODEL_NAME}",
        serving_container_predict_route=f"/v1/models/{MODEL_NAME}:predict",
        serving_container_environment_variables={"MODEL_NAME": MODEL_NAME},       
    )
    
    
    model_deploy = model_upload.deploy(
        machine_type="n1-standard-4", 
        endpoint=endpoint,
        traffic_split={"0": 100},
        deployed_model_display_name=DISPLAY_NAME,
    )
    

    # Save data to the output params
    vertex_model.uri = model_deploy.resource_name
    
