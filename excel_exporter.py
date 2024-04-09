import pandas as pd
import os
from datetime import datetime
from config import EXCEL_EXPORT_PATH

def ensure_directory_exists(path):
    """Ensure the directory for exporting Excel files exists."""
    if not os.path.exists(path):
        os.makedirs(path)

def export_to_excel(data, filename=None):
    """
    Export given data to an Excel file.

    :param data: List of dictionaries, where each dictionary contains data for one row.
    :param filename: Optional. The name of the Excel file to create. If not provided, a name is generated.
    :return: The path to the created Excel file.
    """
    ensure_directory_exists(EXCEL_EXPORT_PATH)
    
    if not filename:
        # Generate a filename with a timestamp if none is provided
        filename = f"inspection_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    file_path = os.path.join(EXCEL_EXPORT_PATH, filename)

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)

    # Use the DataFrame's to_excel method to write to an Excel file
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    return file_path

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = [
        {'Part Number': 'A123', 'Description': 'Valve', 'Quantity': 10, 'Status': 'Passed'},
        {'Part Number': 'B456', 'Description': 'Bearing', 'Quantity': 15, 'Status': 'Failed'},
        # Add more rows as needed
    ]

    # Export to Excel
    file_path = export_to_excel(sample_data)
    print(f"Data exported to Excel file at: {file_path}")
