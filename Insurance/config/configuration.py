
from tkinter import E
# This entity functions gives the structure what configuration information we want to spesify in config folder
from insurance.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig,ModelEvaluationConfig,  ModelPusherConfig, ModelTrainerConfig, TrainingPipelineConfig
from insurance.exception import insuranceException
from insurance.logger import logging
from insurance.util.util import read_yaml_file
import sys , os
from insurance.constant import *


class Configuration:

    def __init__(self,
        config_file_path:str = CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP
        ) -> None:
        try:
            self.config_info = read_yaml_file(file_path = config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e :
            raise insuranceException(e,sys) from e



    def get_training_pipeline_config(self) -> TrainingPipelineConfig :
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise insuranceException(e,sys) from e
