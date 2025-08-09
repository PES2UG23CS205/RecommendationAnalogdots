import pandas as pd
import os

def load_data(data_path='data'):
    """
    Loads user, shoe, and interaction data from CSV files.

    Args:
        data_path (str): The path to the directory containing the data files.

    Returns:
        tuple: A tuple containing three pandas DataFrames:
               (users_df, shoes_df, interactions_df).
    """
    users_path = os.path.join(data_path, 'users.csv')
    shoes_path = os.path.join(data_path, 'shoes.csv')
    interactions_path = os.path.join(data_path, 'interactions.csv')

    try:
        users_df = pd.read_csv(users_path)
        shoes_df = pd.read_csv(shoes_path)
        interactions_df = pd.read_csv(interactions_path)
        
        # Convert timestamp to datetime objects for time-based logic
        interactions_df['timestamp'] = pd.to_datetime(interactions_df['timestamp'])
        
        print("Data loaded successfully.")
        return users_df, shoes_df, interactions_df
    except FileNotFoundError as e:
        print(f"Error loading data: {e}. Make sure the data files are in the '{data_path}' directory.")
        return None, None, None