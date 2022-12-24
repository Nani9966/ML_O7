from sensor.predictor import ModelResolver
from sensor.entity.config_entity import ModelPusherConfig
from sensor.exception import SensorException
import os,sys
from sensor.utils import load_object,save_object
from sensor.logger import logging

from sensor.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact,ModelPusherArtifact


class ModelPusher:
    def __init__(self,model_pusher_config:ModelPusherConfig,
                    data_transformation_artifact:DataTransformationArtifact,
                    model_trainer_artifact:ModelTrainerArtifact

    ):
        try:
            self.model_pusher_config=model_pusher_config
            self.data_transformation_artifact=data_transformation_artifact
            self.model_trainer_artifact=model_trainer_artifact 
            self.model_resolver=ModelResolver(model_registry=self.model_pusher_config.saved_model_dir)
        except Exception as e:
            raise SensorException(e,sys)

    def initiater_model_pusher(self,)->ModelPusherArtifact:
        try:

            #load Object
            logging.info(f"loading transformaer model and target encoder")
            transformer = load_object(file_path = self.data_transformation_artifact.transform_object_path)
            model = load_object(file_path =self.model_trainer_artifact.model_path)
            target_encoder=load_object(file_path = self.data_transformation_artifact.target_encoder_path)
            

            ##model pusher dir
            save_object(file_path=self.model_pusher_config.pusher_transformer_path, obj=transformer)
            save_object(file_path=self.model_pusher_config.pusher_model_path, obj=model)
            save_object(file_path=self.model_pusher_config.pusher_target_encoder_path, obj=target_encoder)


            ##saved model dir 
            transformer_path=self.model_resolver.get_latest_save_transformer_path()
            model_path=self.model_resolver.get_latest_save_model_path()
            target_encoder_path=self.model_resolver.get_latest_target_encoder_path()



            save_object(file_path=transformer_path, obj=transformer)
            save_object(file_path=model_path, obj=model)
            save_object(file_path=target_encoder_path, obj=target_encoder)

        except Exception as e:
            raise SensorException(e,sys)