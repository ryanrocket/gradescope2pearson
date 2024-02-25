# Ryan Wans 2024
from transfer import *

def runBatch(batch: Union[Path, str], preferred_names: Union[Path, str] = None):
    # read batch file
    batch = read_json_file(batch)
    # transfer grades for each file in batch
    for inputFile in batch.keys():
        print(f"Processing {inputFile}...")
        transfer(Path(inputFile), Path(batch[inputFile]), preferred_names)
        
if __name__ == "__main__":
    try:
        batch_file = sys.argv[1]
    except IndexError:
        print("Usage: python batch.py batch_file.json")
        sys.exit(1)
    try:
        preferred_names = sys.argv[2]
    except IndexError:
        preferred_names = None
    
    if batch_file.split(".")[-1] != "json":
        print("Batch file must be .json")
        sys.exit(1)
    elif preferred_names and preferred_names.split(".")[-1] != "json":
        print("Preferred names file must be .json")
        sys.exit(1)
    else:
        print("Batch file: " + batch_file)
        print("Starting batch transfer process...")
        runBatch(batch_file, preferred_names)
        print("Batch transfer process completed.")