# Step 1: Create a new Python script db_utils.py which will contain your code to extract the data from the database. 
from sqlalchemy import create_engine
import pandas as pd
import yaml

#Step 2: Within the script create a new class called RDSDatabaseConnector. This class will contain the methods which you will use to extract data from the RDS database.
class RDSDatabaseConnector:

    #Step 4: Write the __init__ method of your RDSDatabaseConnector class. It should take in as a parameter a dictionary of credentials which your function from the previous step will extract. 
    def __init__(self, credentials_file):
        """
        Initialize the RDSDatabaseConnector with credentials.

        Parameters:
        - credentials_file (str): Path to the YAML file containing database credentials.
        """
        self.credentials = self.load_credentials(credentials_file)
        self.engine = self.create_engine()

    def load_credentials(self, credentials_file):
        """
        Load database credentials from a YAML file.

        Parameters:
        - credentials_file (str): Path to the YAML file containing database credentials.

        Returns:
        - dict: Database credentials.
        """
        with open(credentials_file, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials

    #Step 5: Define a method in your RDSDatabaseConnector class which initialises a SQLAlchemy engine from the credentials provided to your class. This engine object together with the Pandas library will allow you to extract data from the database. 
    def create_engine(self):
        """
        Create a SQLAlchemy engine using the loaded credentials.

        Returns:
        - sqlalchemy.engine.base.Engine: SQLAlchemy engine object.
        """
        engine = create_engine(
            f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@" +
            f"{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        )
        return engine


    #Step 6: Develop a method which extracts data from the RDS database and returns it as a Pandas DataFrame. The data is stored in a table called loan_payments. 
    def extract_data_to_dataframe(self, query):
        """
        Extract data from the database using a SQL query and return as a DataFrame.

        Parameters:
        - query (str): SQL query to extract data.

        Returns:
        - pd.DataFrame: DataFrame containing the extracted data.
        """
        with self.engine.connect() as connection:
            df = pd.read_sql(query, connection)
        return df


    #Step 7: Now create another function which saves the data to an appropriate file format to your local machine. This should speed up loading up the data when you're performing your EDA/analysis tasks. The function should save the data in .csv format, since we're dealing with tabular data.
    def save_data_to_csv(self, df, filename):
        """
        Save DataFrame to a CSV file.

        Parameters:
        - df (pd.DataFrame): DataFrame to save.
        - filename (str): Name of the CSV file.
        """
        df.to_csv(filename, index=False)







   
