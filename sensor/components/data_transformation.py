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


class DataTransformation:


    def __init__(self,data_transformation_config:config_entity.DataTransformConfig,
                      data_ingestion_artifact:artifact_entity.DataIngestionArtifact):

            try:
                self.data_transformation_config=data_transformation_config
                self.data_ingestion_artifact=data_ingestion_artifact


            except Exception as e:
                raise SensorException(e,sys)


    )