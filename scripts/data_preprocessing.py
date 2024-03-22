import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Define a function to load data
def load_data(filepath):
    """Load and return the dataset from the specified filepath."""
    return pd.read_csv(filepath)

# Data preprocessing steps
def preprocess_data(data):
    """
    Preprocess the data: clean, encode, and scale the data.

    Args:
    data (DataFrame): The input data to be preprocessed.

    Returns:
    DataFrame: The processed data ready for modeling.
    """
    
    # Identify the numerical columns and categorical columns
    numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = data.select_dtypes(include=['object', 'bool']).columns

    # Preprocessing for numerical data
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),  # Handling missing values
        ('scaler', StandardScaler())  # Standardizing data
    ])

    # Preprocessing for categorical data
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),  # Handling missing values
        ('onehot', OneHotEncoder(handle_unknown='ignore'))  # One-hot encoding
    ])

    # Bundle preprocessing for numerical and categorical data
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])

    # Apply the preprocessing pipelines to the data
    processed_data = preprocessor.fit_transform(data)

    return processed_data

if __name__ == "__main__":
    # Example usage
    dataset_path = 'path/to/your/dataset.csv'
    data = load_data(dataset_path)
    processed_data = preprocess_data(data)

    print("Data preprocessing completed successfully.")
    # Further code to utilize the processed_data, such as saving or additional processing