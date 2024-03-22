import unittest
import pandas as pd
import numpy as np
from data_preprocessing import preprocess_data

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        """Initialize the dataset before each test."""
        self.data = pd.DataFrame({
            'age': [25, np.nan, 30, 35, 40],
            'income': [50000, 60000, np.nan, 100000, 90000],
            'gender': ['male', 'female', 'female', np.nan, 'male'],
            'purchased': [1, 0, 1, 0, 1]
        })

    def test_missing_values(self):
        """Test if the missing values are handled correctly."""
        processed_data = preprocess_data(self.data)

        # Check if there are no missing values in the processed data
        self.assertFalse(processed_data.isnull().values.any())

    def test_feature_scaling(self):
        """Test if numerical features are scaled properly."""
        processed_data = preprocess_data(self.data)

        # Assuming standard scaling is applied, mean should be close to 0 and std close to 1
        for column in processed_data.select_dtypes(include=[np.number]):
            self.assertAlmostEqual(processed_data[column].mean(), 0, delta=0.1)
            self.assertAlmostEqual(processed_data[column].std(), 1, delta=0.1)

    def test_categorical_encoding(self):
        """Test if categorical features are encoded correctly."""
        processed_data = preprocess_data(self.data)

        # Check if 'gender' column is transformed into appropriate number of dummy variables
        # Assuming 'gender' is the only categorical feature
        expected_columns = 2  # Adjust based on the number of categories expected after encoding
        encoded_columns = len([col for col in processed_data.columns if 'gender' in col])

        self.assertEqual(encoded_columns, expected_columns)

    # Add more tests as needed to cover all aspects of your preprocessing

if __name__ == '__main__':
    unittest.main()