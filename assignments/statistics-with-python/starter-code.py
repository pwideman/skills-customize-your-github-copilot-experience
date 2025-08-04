"""
Statistics with Python Assignment - Starter Code
Mergington High School Computer Science

Student Name: _______________
Date: _______________

Instructions:
1. Complete the functions below to perform statistical analysis
2. Run the code with the provided sample dataset
3. Answer the reflection questions at the bottom
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_and_explore_data(filename):
    """
    Load CSV data and perform initial exploration
    
    Args:
        filename (str): Path to the CSV file
    
    Returns:
        pandas.DataFrame: The loaded dataset
    """
    # TODO: Load the CSV file using pandas
    df = None
    
    # TODO: Print basic information about the dataset
    # Hint: Use .info(), .shape, .head(), .tail()
    
    # TODO: Check for missing values
    # Hint: Use .isnull().sum()
    
    # TODO: Generate summary statistics
    # Hint: Use .describe()
    
    return df

def calculate_statistics(df, column_name):
    """
    Calculate comprehensive statistics for a numerical column
    
    Args:
        df (pandas.DataFrame): The dataset
        column_name (str): Name of the column to analyze
    
    Returns:
        dict: Dictionary containing statistical measures
    """
    stats = {}
    
    # TODO: Calculate mean, median, mode
    stats['mean'] = None
    stats['median'] = None
    stats['mode'] = None
    
    # TODO: Calculate standard deviation and variance
    stats['std'] = None
    stats['variance'] = None
    
    # TODO: Calculate min, max, quartiles
    stats['min'] = None
    stats['max'] = None
    stats['q1'] = None
    stats['q3'] = None
    
    return stats

def analyze_correlations(df):
    """
    Calculate and visualize correlations between numerical columns
    
    Args:
        df (pandas.DataFrame): The dataset
    """
    # TODO: Select only numerical columns
    numerical_cols = None
    
    # TODO: Calculate correlation matrix
    correlation_matrix = None
    
    # TODO: Create a heatmap of correlations
    # Hint: Use plt.figure(), plt.imshow(), plt.colorbar()
    
    return correlation_matrix

def group_analysis(df, group_column, value_column):
    """
    Perform groupby analysis to compare statistics across groups
    
    Args:
        df (pandas.DataFrame): The dataset
        group_column (str): Column to group by
        value_column (str): Column to analyze
    
    Returns:
        pandas.DataFrame: Summary statistics by group
    """
    # TODO: Group data and calculate statistics
    grouped_stats = None
    
    # TODO: Create a bar chart comparing groups
    # Hint: Use .plot(kind='bar')
    
    return grouped_stats

def main():
    """
    Main function to run the statistical analysis
    """
    # TODO: Load your dataset
    data_file = "sample_data.csv"  # Replace with your dataset
    df = load_and_explore_data(data_file)
    
    if df is not None:
        # TODO: Choose a numerical column for detailed analysis
        column_to_analyze = "column_name"  # Replace with actual column name
        stats = calculate_statistics(df, column_to_analyze)
        print(f"Statistics for {column_to_analyze}:")
        for stat, value in stats.items():
            print(f"{stat}: {value}")
        
        # TODO: Analyze correlations
        correlations = analyze_correlations(df)
        
        # TODO: Perform group analysis
        # Replace with appropriate column names from your dataset
        group_col = "category_column"
        value_col = "numerical_column"
        grouped_results = group_analysis(df, group_col, value_col)
        
        # TODO: Export results
        # df.to_csv("analysis_results.csv", index=False)

if __name__ == "__main__":
    main()

"""
Reflection Questions (Answer after completing the assignment):

1. What was the most interesting pattern you discovered in your data?


2. Which statistical measure (mean, median, mode) best represents your data and why?


3. What correlations did you find? Were any surprising?


4. How could this type of analysis be useful in real-world scenarios?


5. What challenges did you face while working with the data?

"""
