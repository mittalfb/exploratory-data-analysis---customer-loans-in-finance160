
import pandas as pd

class DataFrameInfo:
    @staticmethod
    def describe_columns(df):
      
        return df.dtypes.to_frame(name='Data Type')

    @staticmethod
    def extract_statistical_values(df):
       
        return df.describe().transpose()[['mean', 'std', '50%']]

    @staticmethod
    def count_distinct_values(df):
       
        return df.select_dtypes(include=['category']).nunique().to_frame(name='Count Distinct')

    @staticmethod
    def print_shape(df):
      
        print("DataFrame Shape:", df.shape)

    @staticmethod
    def generate_null_count(df):
       
        return df.isnull().sum()

    @staticmethod
    def generate_null_percentage(df):
       
        return (df.isnull().sum() / len(df)) * 100
