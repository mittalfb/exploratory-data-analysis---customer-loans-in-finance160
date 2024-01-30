
import pandas as pd

class DataFrameInfo:
    @staticmethod
    def describe_columns(df):
        """
        Describe all columns in the DataFrame to check their data types.

        Parameters:
        - df (pd.DataFrame): DataFrame to describe.

        Returns:
        - pd.DataFrame: Description of columns with their data types.
        """
        return df.dtypes.to_frame(name='Data Type')

    @staticmethod
    def extract_statistical_values(df):
        """
        Extract statistical values: median, standard deviation, and mean from the columns and the DataFrame.

        Parameters:
        - df (pd.DataFrame): DataFrame to extract statistical values from.

        Returns:
        - pd.DataFrame: Statistical values for each column and the DataFrame.
        """
        return df.describe().transpose()[['mean', 'std', '50%']]

    @staticmethod
    def count_distinct_values(df):
        """
        Count distinct values in categorical columns.

        Parameters:
        - df (pd.DataFrame): DataFrame to count distinct values from.

        Returns:
        - pd.DataFrame: Count of distinct values for each categorical column.
        """
        return df.select_dtypes(include=['category']).nunique().to_frame(name='Count Distinct')

    @staticmethod
    def print_shape(df):
        """
        Print out the shape of the DataFrame.

        Parameters:
        - df (pd.DataFrame): DataFrame to print shape of.
        """
        print("DataFrame Shape:", df.shape)

    @staticmethod
    def generate_null_count(df):
        """
        Generate a count of NULL values in each column.

        Parameters:
        - df (pd.DataFrame): DataFrame to count NULL values from.

        Returns:
        - pd.Series: Count of NULL values for each column.
        """
        return df.isnull().sum()

    @staticmethod
    def generate_null_percentage(df):
        """
        Generate a percentage count of NULL values in each column.

        Parameters:
        - df (pd.DataFrame): DataFrame to count NULL values from.

        Returns:
        - pd.Series: Percentage of NULL values for each column.
        """
        return (df.isnull().sum() / len(df)) * 100

