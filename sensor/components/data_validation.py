
from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
import os,sys
from typing import Optional




class DataValidation:

    def __init__(self,data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} Data validation {'<<'*20}")
            self.data_validation_config=data_validation_config
        except Exception as e:
            raise  SensorException(e,sys)


    def  drop_missing_columns(self,df:pd.DataFrame)->option [pd.DataFrame]:
        """ 
        This function will drop columns which contain missing values mortethan specified thersold
        df :Accepts a pandas dataframe 
        thershold:percentage criteria to drop a column
        ================================
        return pandas DataFrame if atleast a single column is avalibleafter missing column drop else  None

        """
        try:
            thershold =self.data_validation_config.missing_threshold
            
            null_report=df.isna().sum()/df.shape[0]
            #selecting column namewhich coontains null values
            drop_column_names=null_report[null_report>thershold].index
            df.drop(list(drop_columns_names),axis=1,implace =True)

            #return None no columns left

            if len(df.columns)==0:
                return None

            return df


                    
        except Exception as e:
            raise e


    def is_required_columsn_exists(self,base_df,present_df)->bool:
        
        try:
            pass
        except Exception as e:
            raise e



    def initiate_data_validation(self) ->artifact_entity.DataValidationArtifact:
        pass
