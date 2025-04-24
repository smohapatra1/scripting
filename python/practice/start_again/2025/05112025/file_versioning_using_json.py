#   https://www.geeksforgeeks.org/file-versioning-in-python/
import json
import os
import shutil
import datetime

def version_file_with_metadata(file_path):
    if os.path.exists(file_path):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        versioned_file = f"{file_path}.{timestamp}"
        shutil.copyfile(file_path, versioned_file)

        # Save metadata
        metadata = {"original_file": file_path, "timestamp": timestamp}
        metadata_file = f"{versioned_file}.json"
        with open(metadata_file, "w") as f:
            json.dump(metadata, f)

        print(f"Version created: {versioned_file}")
        print(f"Metadata saved: {metadata_file}")
    else:
        print("File not found.")

# Example usage:
file_path = "file.txt"
version_file_with_metadata(file_path)