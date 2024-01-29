
import pandas as pd
import numpy as np
from scipy.stats import zscore

class DataTransform:
    @staticmethod
    def convert_to_numeric(df, columns):
       
        df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')

    @staticmethod
    def convert_to_datetime(df, columns):
        
        df[columns] = pd.to_datetime(df[columns], errors='coerce')

    @staticmethod
    def convert_to_categorical(df, columns):
       
        df[columns] = df[columns].astype('category')

    @staticmethod
    def remove_symbols(df, columns, symbols):
       
        if isinstance(symbols, str):
            symbols = [symbols]
        for symbol in symbols:
            df[columns] = df[columns].replace(symbol, '', regex=True)

    @staticmethod
    def find_null_percentage(df):
       
        null_percentage = (df.isnull().sum() / len(df)) * 100
        return null_percentage

    @staticmethod
    def drop_columns_with_nulls(df, threshold=30):
       
        null_percentage = DataTransform.find_null_percentage(df)
        columns_to_drop = null_percentage[null_percentage > threshold].index
        df = df.drop(columns=columns_to_drop)
        return df

    @staticmethod
    def impute_nulls(df, strategy='median'):
       
        if strategy == 'median':
            df = df.fillna(df.median())
        elif strategy == 'mean':
            df = df.fillna(df.mean())
        return df

    @staticmethod
    def transform_skewed_columns(df, skewed_columns):
       
        for column in skewed_columns:
            # Log transformation
            df[column] = np.log1p(df[column])
            # You can try other transformations like square root, cube root, etc.

        return df

    @staticmethod
    def remove_outliers(df, z_threshold=3):
       
        # Calculate Z-scores
        z_scores = np.abs(zscore(df))

        # Create a mask to identify outliers
        outliers_mask = (z_scores > z_threshold).any(axis=1)

        # Remove outliers
        df_no_outliers = df[~outliers_mask]

        return df_no_outliers

    @staticmethod
    def remove_highly_correlated_columns(df, threshold=0.8):
       
        # Compute the correlation matrix
        correlation_matrix = df.corr().abs()

        # Create a mask for highly correlated columns
        mask = correlation_matrix.apply(lambda x: any(x > threshold), axis=0)

        # Drop highly correlated columns
        df_no_high_corr = df.drop(columns=correlation_matrix.columns[mask])

        return df_no_high_corr
