
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:

    #Step 4: Run your NULL checking method/function again to check that all NULLs have been removed. Generate a plot by creating a method in your Plotter class to visualise the removal of NULL values.
    @staticmethod
    def visualize_null_removal(before_df, after_df):
        """
        Visualize the removal of NULL values in a DataFrame.

        Parameters:
        - before_df (pd.DataFrame): DataFrame before removing NULL values.
        - after_df (pd.DataFrame): DataFrame after removing NULL values.
        """
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        sns.heatmap(before_df.isnull(), cbar=False, cmap='viridis')
        plt.title('Before NULL Removal')

        plt.subplot(1, 2, 2)
        sns.heatmap(after_df.isnull(), cbar=False, cmap='viridis')
        plt.title('After NULL Removal')

        plt.tight_layout()
        plt.show()

    @staticmethod
    def visualize_skewness(df, skewed_columns):
        """
        Visualize the skewness of specified columns in the DataFrame.

        Parameters:
        - df (pd.DataFrame): DataFrame to visualize.
        - skewed_columns (list): List of column names with skewness.
        """
        plt.figure(figsize=(12, 6))
        for i, column in enumerate(skewed_columns, 1):
            plt.subplot(1, len(skewed_columns), i)
            sns.histplot(df[column], kde=True)
            plt.title(f'Skewness: {df[column].skew():.2f}\n{column}')

        plt.tight_layout()
        plt.show()


  #Step 3: With the outliers transformed/removed re-visualise your data with you Plotter class to check that the outliers have been correctly removed. 
    @staticmethod
    def visualize_outliers(df):
        """
        Visualize potential outliers in the DataFrame.

        Parameters:
        - df (pd.DataFrame): DataFrame to visualize.
        """
        plt.figure(figsize=(12, 6))
        for i, column in enumerate(df.columns, 1):
            plt.subplot(1, len(df.columns), i)
            sns.boxplot(x=df[column])
            plt.title(f'Boxplot of {column}')

        plt.tight_layout()
        plt.show()

    @staticmethod
    def visualize_correlation_matrix(correlation_matrix):
        """
        Visualize the correlation matrix.

        Parameters:
        - correlation_matrix (pd.DataFrame): Correlation matrix.
        """
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        plt.title('Correlation Matrix')
        plt.show()
