from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
from sensor.exception import SensorException
import os , sys
from sensor.logger import logging
from  sensor.utils2 import dump_csv_file_to_mongodb_collection
from sensor.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig

from sensor.pipeline.training_pipeline import TrainPipeline
from fastapi import FastAPI
from sensor.constant.application import APP_HOST,APP_PORT
from uvicorn import run as app_run
from starlette.responses import RedirectResponse
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI, File, UploadFile,Response
import pandas as pd


app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers =["*"])


@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train")
async def train ():

    try:

        training_pipeline = TrainPipeline()

        if training_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")

        training_pipeline.run_pipeline()

        return Response("Training successful completed!!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

# @app.get("/predict")
# async def predict():
#
#     try:
#
#         #get data from csv file
#         #convert it into dataframe
#
#         df = None
#         Model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
#         if not Model_resolver.is_model_exists():
#             return Response("Model is not available")
#
#         best_model_path = Model_resolver.get_best_model_path()
#         model = load_object(file_path=best_model_path)
#         y_pred = model.predict(df)
#         df["predicted_column"] = y_pred
#         df["predicted_column"].replace(TargetValueMapping().reverse_mapping(), inplace=True)
#
#         #get the predicted output as you want
#     except Exception as e:
#         raise SensorException(e,sys)



#need to correct it for prediction
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Step 1: Read data from the uploaded CSV file
        df = pd.read_csv(file.file)

        # Step 2: Check if the model exists
        Model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not Model_resolver.is_model_exists():
            return Response("Model is not available")

        # Step 3: Load the best model and make predictions
        best_model_path = Model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        y_pred = model.predict(df)

        # Step 4: Process predictions and add them to the DataFrame
        df["predicted_column"] = y_pred
        df["predicted_column"].replace(TargetValueMapping().reverse_mapping(), inplace=True)

        # Step 5: Convert the DataFrame with predictions to JSON and return it as a response
        result = df.to_dict(orient="records")
        return result

    except Exception as e:
        raise SensorException(e, sys)



def main():
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()

    except Exception as e:
        print(e)
        logging.exception(e)
if __name__ == "__main__":

    # file_path="aps_failure_training_set1.csv"
    # database_name="mldb"
    # collection_name ="col"
    # # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)



    app_run(app,host= APP_HOST,port=APP_PORT)









  










