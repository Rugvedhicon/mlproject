#!/usr/bin/env python3
"""
Test script to debug data.csv access issues
"""

import os
import pandas as pd

def test_data_access():
    print("=== Testing data.csv access ===")
    
    # Check current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # Check if Data directory exists
    data_dir_exists = os.path.exists('Data')
    print(f"Data directory exists: {data_dir_exists}")
    
    # Check if data.csv exists
    data_file_exists = os.path.exists('Data/data.csv')
    print(f"Data/data.csv exists: {data_file_exists}")
    
    # List contents of Data directory
    if data_dir_exists:
        print(f"Contents of Data directory: {os.listdir('Data')}")
    
    # Try to read the file
    try:
        print("\nAttempting to read data.csv...")
        df = pd.read_csv('Data/data.csv')
        print(f"✅ SUCCESS! Data loaded successfully.")
        print(f"Data shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst 3 rows:")
        print(df.head(3))
        
    except FileNotFoundError as e:
        print(f"❌ FileNotFoundError: {e}")
        print("Try running this script from the project root directory (mlproject)")
        
    except PermissionError as e:
        print(f"❌ PermissionError: {e}")
        print("Check file permissions")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print(f"Error type: {type(e)}")

if __name__ == "__main__":
    test_data_access()
