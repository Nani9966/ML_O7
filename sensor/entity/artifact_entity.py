

from dataclasses import dataclass

@dataclass 
class DataIngestionArtifact:
    feature_store_file_path:str 
    train_file_path:str 
    test_file_path:str 

@dataclass
class DataValidationArtifact:
    report_file_path:str



class DataValidationArtifact:
    report_file_path:str
    
class DataTransformationArtifact:...
class DataTrainerArtifact:...
class ModelEvaluationArtifact:...
class ModelPusherArtifact:...

