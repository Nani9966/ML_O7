import os
from sensor.entity.config_entity import TRANSFORMER_OBJECT_FILE_NAME ,MODEL_FILE_NAME,TARGET_ENCODER_OBJECT_FILE_NAME
from glob import glob
class ModelResolver:

    def __init__(self,model_registry:str="saved_models",
                    transformer_dir_name="transformer",
                    target_encoder_dir_name= "target_encoder",
                    model_dir_name = "model"):
        self.model_registry=model_registry
        self.transformer_dir_name=transformer_dir_name
        self.target_encoder_dir_name=target_encoder_dir_name
        self.model_dir_name=model_dir_name

    def get_latest_dir_path(self):
        try:
            dir_names = os.listdir(self.model_registry)
            dir_names=list(map(int,dir_names))
            latest_dir_name=max(dir_names)
            return os.path.join(self.model_registry,f"{latest_folder_name}")
        except Exception as e:
            return e

    
    def get_latest_dir_model_path(self):
        try:
            latest_dir=self.get_latest_dir_model_path()
            return os.path.join(latest_dir,self.model_dir_name,MODEL_FILE_NAME)
        except Exception as e:
            return e

    def get_latest_transformer_path(self):
        try:
            latest_dir=self.get_latest_dir_model_path()
            return os.path.join(latest_dir,self.transformer_dir_name,TRANSFORMER_OBJECT_FILE_NAME)
        except Exception as e:
            return e
    def get_latest_target_encoder_path(self):
        try:
            latest_dir=self.get_latest_dir_model_path()
            return os.path.join(latest_dir,self.target_encoder_dir_name,TARGET_ENCODER_OBJECT_FILE_NAME)
        except Exception as e:
            return e

    def get_latest_save_dir_path(self):
        try:
            latest_folder_num=int(os.path.basename(self.get_latest_dir_path()))
        except Exception as e:
            return e


class Predictor:
    def __init__(self,model_resorvior)