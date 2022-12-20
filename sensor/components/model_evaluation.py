from sensor.predictor import ModelResolver
from sensor.entity import config_entity,artifact_entity


class ModelEvaluation:
    def __init__(self,
    model_eval_config:config_entity.ModelEvaluationConfig,
    data_ingestion_artifact:artifact_entity.DataIngestionArtifact,
    data_transformation_artifact:artifact_entity.DataTransformationArtifact,
    model_trainer_artifact:artifact_entity.ModelTrainerArtifact
    ):
        try:
          self.model_eval_config=model_eval_config
          self.data_ingestion_artifact=data_ingestion_artifact
          self.data_ingestion_artifact=data_transformation_artifact
          self.model_trainer_artifact=model_trainer_artifact
          self.model_resolver=ModelEvaluation()
        except Exception as e:
            raise SensorException(e,sys)

    def initiate_model_evaluation() -> artifact_entity.ModelEvaluationArtifact:
        try:
            ##if saved model folder has model the we will compare
            #which model is best trained or the mdoel from saved model folder
            latest_dir_path=self.model_resolver.get_latest_dir_path()
            if latest_dir_path == None:
                model_eval_artifact=artifact_entity.ModelEvaluationArtifact(is_model_accepted=True,
                imporved_accuracy=None)

                return  model_eval_artifact

        except Exception as e:
            raise SensorException(e,sys)