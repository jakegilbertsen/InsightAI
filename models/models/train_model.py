import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def load_data(filepath):
    """Load dataset from a specified filepath."""
    data = pd.read_csv(filepath)
    return data

def preprocess_data(data):
    """Preprocess the data: dummy example of dropping NA and encoding categories."""
    data = data.dropna()
    data = pd.get_dummies(data)
    return data

def train_model(X_train, y_train):
    """Train a machine learning model (Random Forest Classifier in this case)."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model's performance on the test set."""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    print("Model Accuracy:", accuracy)
    print("Classification Report:\n", report)

def save_model(model, filename):
    """Save the trained model as a joblib file."""
    joblib.dump(model, filename)

if __name__ == '__main__':
    # Define file paths
    dataset_path = 'path/to/your/dataset.csv'
    model_save_path = 'path/to/save/your_model.joblib'

    # Load and preprocess the data
    data = load_data(dataset_path)
    data = preprocess_data(data)

    # Split the data into training and test sets
    X = data.drop('target_column', axis=1)
    y = data['target_column']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the model
    save_model(model, model_save_path)

    print(f"Model trained and saved successfully at {model_save_path}")