
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    @staticmethod
    def visualize_null_removal(before_df, after_df):
       
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
        
        plt.figure(figsize=(12, 6))
        for i, column in enumerate(skewed_columns, 1):
            plt.subplot(1, len(skewed_columns), i)
            sns.histplot(df[column], kde=True)
            plt.title(f'Skewness: {df[column].skew():.2f}\n{column}')

        plt.tight_layout()
        plt.show()

    @staticmethod
    def visualize_outliers(df):
       
        plt.figure(figsize=(12, 6))
        for i, column in enumerate(df.columns, 1):
            plt.subplot(1, len(df.columns), i)
            sns.boxplot(x=df[column])
            plt.title(f'Boxplot of {column}')

        plt.tight_layout()
        plt.show()

    @staticmethod
    def visualize_correlation_matrix(correlation_matrix):
       
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        plt.title('Correlation Matrix')
        plt.show()
