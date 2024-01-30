
import pandas as pd
import numpy as np
from scipy.stats import zscore

class DataTransform:
    @staticmethod
    def convert_to_numeric(df, columns):
        """
        Convert specified columns to numeric format.

        Parameters:
        - df (pd.DataFrame): DataFrame to perform conversions on.
        - columns (list): List of column names to convert to numeric.
        """
        df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')

    @staticmethod
    def convert_to_datetime(df, columns):
        """
        Convert specified columns to datetime format.

        Parameters:
        - df (pd.DataFrame): DataFrame to perform conversions on.
        - columns (list): List of column names to convert to datetime.
        """
        df[columns] = pd.to_datetime(df[columns], errors='coerce')

    @staticmethod
    def convert_to_categorical(df, columns):
        """
        Convert specified columns to categorical format.

        Parameters:
        - df (pd.DataFrame): DataFrame to perform conversions on.
        - columns (list): List of column names to convert to categorical.
        """
        df[columns] = df[columns].astype('category')

    @staticmethod
    def remove_symbols(df, columns, symbols):
        """
        Remove specified symbols from DataFrame columns.

        Parameters:
        - df (pd.DataFrame): DataFrame to remove symbols from.
        - columns (list): List of column names to remove symbols from.
        - symbols (str or list): Symbols to remove.
        """
        if isinstance(symbols, str):
            symbols = [symbols]
        for symbol in symbols:
            df[columns] = df[columns].replace(symbol, '', regex=True)

    @staticmethod
    def find_null_percentage(df):
        """
        Find the percentage of NULL values in each column.

        Parameters:
        - df (pd.DataFrame): DataFrame to check for NULL values.

        Returns:
        - pd.Series: Percentage of NULL values for each column.
        """
        null_percentage = (df.isnull().sum() / len(df)) * 100
        return null_percentage

    @staticmethod
    def drop_columns_with_nulls(df, threshold=30):
        """
        Drop columns with a percentage of NULL values above the threshold.

        Parameters:
        - df (pd.DataFrame): DataFrame to drop columns from.
        - threshold (float): Percentage threshold for NULL values. Default is 30.

        Returns:
        - pd.DataFrame: DataFrame after dropping columns.
        """
        null_percentage = DataTransform.find_null_percentage(df)
        columns_to_drop = null_percentage[null_percentage > threshold].index
        df = df.drop(columns=columns_to_drop)
        return df

    @staticmethod
    def impute_nulls(df, strategy='median'):
        """
        Impute NULL values in the DataFrame using specified strategy.

        Parameters:
        - df (pd.DataFrame): DataFrame to impute NULL values.
        - strategy (str): Imputation strategy ('median' or 'mean'). Default is 'median'.

        Returns:
        - pd.DataFrame: DataFrame after imputing NULL values.
        """
        if strategy == 'median':
            df = df.fillna(df.median())
        elif strategy == 'mean':
            df = df.fillna(df.mean())
        return df

    @staticmethod
    def transform_skewed_columns(df, skewed_columns):
        """
        Apply transformations to reduce skewness in specified columns.

        Parameters:
        - df (pd.DataFrame): DataFrame to transform.
        - skewed_columns (list): List of column names with skewness.

        Returns:
        - pd.DataFrame: DataFrame after applying transformations.
        """
        for column in skewed_columns:
            # Log transformation
            df[column] = np.log1p(df[column])
            # You can try other transformations like square root, cube root, etc.

        return df

    @staticmethod
    def remove_outliers(df, z_threshold=3):
        """
        Remove outliers from the DataFrame using Z-score.

        Parameters:
        - df (pd.DataFrame): DataFrame to remove outliers from.
        - z_threshold (float): Z-score threshold. Default is 3.

        Returns:
        - pd.DataFrame: DataFrame after removing outliers.
        """
        # Calculate Z-scores
        z_scores = np.abs(zscore(df))

        # Create a mask to identify outliers
        outliers_mask = (z_scores > z_threshold).any(axis=1)

        # Remove outliers
        df_no_outliers = df[~outliers_mask]

        return df_no_outliers

    @staticmethod
    def remove_highly_correlated_columns(df, threshold=0.8):
        """
        Remove highly correlated columns from the DataFrame.

        Parameters:
        - df (pd.DataFrame): DataFrame to remove columns from.
        - threshold (float): Correlation threshold. Default is 0.8.

        Returns:
        - pd.DataFrame: DataFrame after removing highly correlated columns.
        """
        # Compute the correlation matrix
        correlation_matrix = df.corr().abs()

        # Create a mask for highly correlated columns
        mask = correlation_matrix.apply(lambda x: any(x > threshold), axis=0)

        # Drop highly correlated columns
        df_no_high_corr = df.drop(columns=correlation_matrix.columns[mask])

        return df_no_high_corr

