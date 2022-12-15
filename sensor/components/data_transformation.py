from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
import os,sys
from typing import Optional
import yaml
import pandas as pd 
from sensor import utils
import numpy as np
from sklearn.preprocessing import Pipeline 
from imblearn.combine import SMOTETomek
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from sensor.config import TARGET_COLUMN
from sklearn.preprocessing import LabelEncoder 




class DataTransformation:


    def __init__(self,data_transformation_config:config_entity.DataTransformConfig,
                      data_ingestion_artifact:artifact_entity.DataIngestionArtifact):

            try:
                self.data_transformation_config=data_transformation_config
                self.data_ingestion_artifact=data_ingestion_artifact


            except Exception as e:
                raise SensorException(e,sys)

    @classmethod
    def get_data_tranformer_object(cls)->Pipeline:
        try:
            simple_imputer=SimpleImputer(strategy="constant",fill_value=0)
            robust_scaler=RobustScaler()

            constant_pipeline=Pipeline(steps=[('Imputer',simple_imputer),('RobustScaler',robust_scaler)])

        except Exception as e:
            raise SensorException(e,sys)

    def initiate_data_transformation(self,)->artifact_entity.DataTransformationArtifact:
        try:
            #reading training and testing file
            train_df=pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df=pd.read_csv(self.data_ingestion_artifact.test_file_path)

            #selecting imput  feature fro and test dataframe    
            input_feature_train=train_df.drop(TARGET_COLUMN,axis=1)
            input_feature_test=test_df.drop(TARGET_COLUMN,axis=1)

            #selecting target feature for train and test dataframe
            target_feature_train_df =train_df[TARGET_COLUMN]
            target_feature_test_df =test_df[TARGET_COLUMN]

            #Lable_encoder

            label_encoder =LabelEncoder()
            label_encoder.fit(target_feature_test_df)

            label_encoder.transform(target_feature_train_df)
            label_encoder.transform(target_feature_test_df)

        except Exception as e:
            raise SensorException(e,sys)


    )