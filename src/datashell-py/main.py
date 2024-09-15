import yaml
import typer
from pathlib import Path
import time

from metadata_reader import get_file_metadata

# yaml_test = "../datashell-py/src/data/test.yaml"

# with open(yaml_test, 'r') as file:
#     data = yaml.safe_load(file)

def dict_to_yaml(data, file_path=None):
    """
    Convert a dictionary to YAML format.
    """
    yaml_file_path = Path(file_path).with_suffix('.yaml')
    print(yaml_file_path)
    try:
        with open(yaml_file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
    except:
        print("lmao")

def main(path: str):
    start_time = time.time()
    
    file_metadata = get_file_metadata(path)
    dict_to_yaml(data=file_metadata, file_path=path)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Execution time: {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    typer.run(main)