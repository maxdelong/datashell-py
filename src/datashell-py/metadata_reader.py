from pathlib import Path
import polars as pl
import pyarrow.parquet as pq

def get_file_metadata(file_path):
    file_path = Path(file_path)
    file_extension = file_path.suffix

    if file_extension == '.csv':
        return get_csv_metadata(file_path)
    elif file_extension == '.parquet':
        return get_parquet_metadata(file_path)
    else:
        return f"Unsupported file type: {file_extension}"

# Define individual metadata functions for each format

def get_csv_metadata(file_path):
    """Extract metadata from a CSV file using Polars."""
    # Read only the first row to get the column names
    df = pl.read_csv(file_path, n_rows=1)
    
    # Get number of rows by counting lines and subtracting the header
    with open(file_path, 'r') as f:
        num_rows = sum(1 for _ in f) - 1  # Subtract header
    
    # Get the number of columns
    num_cols = len(df.columns)
    
    # Get the column names
    column_names = df.columns
    
    return {
        'file_type': 'CSV',
        'num_rows': num_rows,
        'num_columns': num_cols,
        'column_names': column_names
    }


def get_parquet_metadata(file_path):
    """Extract metadata from a Parquet file using PyArrow."""
    parquet_file = pq.ParquetFile(file_path)
    return {
        'file_type': 'Parquet',
        'num_rows': parquet_file.metadata.num_rows,
        'num_columns': parquet_file.metadata.num_columns,
        'schema': str(parquet_file.schema)
    }