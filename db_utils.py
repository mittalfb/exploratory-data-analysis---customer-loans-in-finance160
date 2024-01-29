
from sqlalchemy import create_engine
import pandas as pd
import yaml

class RDSDatabaseConnector:
    def __init__(self, credentials_file):
      
        self.credentials = self.load_credentials(credentials_file)
        self.engine = self.create_engine()

    def load_credentials(self, credentials_file):
      
        with open(credentials_file, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials

    def create_engine(self):
       
        engine = create_engine(
            f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@" +
            f"{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        )
        return engine

    def extract_data_to_dataframe(self, query):
       
        with self.engine.connect() as connection:
            df = pd.read_sql(query, connection)
        return df

    def save_data_to_csv(self, df, filename):
      
        df.to_csv(filename, index=False)




   
