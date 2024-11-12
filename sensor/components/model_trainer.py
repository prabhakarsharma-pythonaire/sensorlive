from pickle import FRAME

from sensor.exception import SensorException
from sensor.utils.main_utils import load_numpy_array_data
from sensor.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from sensor.entity.config_entity import ModelTrainerConfig
import os,sys
from sensor.logger import logging
from xgboost import XGBClassifier
from sensor.ml.metric.classification_metric import get_classification_score
from sensor.ml.model.estimator import SensorModel
from sensor.utils.main_utils import save_object,load_object



class ModelTrainer:

    def __init__(self, model_trainer_config:ModelTrainerConfig,
                 data_transformatoin_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_transformatoin_artifact

        except