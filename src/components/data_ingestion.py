import pandas as pd
import sys
import os

# Add the src directory to the path so we can import our logger
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logger import log_info, log_error, log_warning

class DataIngestion:
    def __init__(self):
        log_info("DataIngestion component initialized")
    
    def load_data(self, file_path):
        """Load data from file"""
        try:
            log_info(f"Attempting to load data from: {file_path}")
            
            if not os.path.exists(file_path):
                log_error(f"File not found: {file_path}")
                raise FileNotFoundError(f"File not found: {file_path}")
            
            # Load data (example with CSV)
            data = pd.read_csv(file_path)
            log_info(f"Successfully loaded data with shape: {data.shape}")
            
            return data
            
        except Exception as e:
            log_error(f"Error loading data: {str(e)}")
            raise
    
    def validate_data(self, data):
        """Validate loaded data"""
        try:
            log_info("Starting data validation")
            
            if data.empty:
                log_warning("Data is empty")
                return False
            
            # Check for missing values
            missing_values = data.isnull().sum().sum()
            if missing_values > 0:
                log_warning(f"Found {missing_values} missing values in the dataset")
            
            log_info("Data validation completed successfully")
            return True
            
        except Exception as e:
            log_error(f"Error during data validation: {str(e)}")
            return False

if __name__ == "__main__":
    # Example usage
    ingestion = DataIngestion()
    log_info("Data ingestion example completed")
