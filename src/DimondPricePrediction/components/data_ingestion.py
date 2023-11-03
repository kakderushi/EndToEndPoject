import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from sklearn.model_selection import trian_test_split
from src.DimondPricePrediction.exception import customexception
from dataclasses import dataclass
from  pathlib import Path
 
class DataIngestionConfig:
     raw_data_path=os.path.join('attifacts','raw.csv')
     train_data_path=os.path.join('attifacts','train.csv')
     test_dataPath=os.path.join('attifacts','test/csv')

class DataINgestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        

        
    def initiate_dataIngestion(self):
        logging.info('data ingestion is started')
        try:
            data=pd.read_csv((os.path.join('notebooks/data','gemstone.csv')))
            logging.info("i have read data set")
            os.makedirs(os.path.join(self.ingestion_config.raw_data_path),exists_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(" i have save the raw data in artifacts folder")
            
            
            
            logging.info("train test split")
            train_data,test_data=trian_test_split(data,test_size=0.25)
            logging.info(" train test split is completed")
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_dataPath,index=False)
            
            logging.info("data ingestion part complted")
            
            
            
        except Exception as e:
            logging.info("Exception during occured at data ingestion stage")
            raise customexception(e,sys)