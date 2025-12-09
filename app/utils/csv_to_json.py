import csv
import json
import sys
from datetime import datetime

def csv_to_json(csv_file_path, json_file_path):
    """
    Convert a CSV file to JSON format with version and locaisColeta structure.
    Handles fields wrapped in quotation marks automatically.
    Empty cells are omitted from the JSON output.
    
    Args:
        csv_file_path: Path to the input CSV file
        json_file_path: Path to the output JSON file
    """
    try:
        # Read CSV file
        locais_coleta = []
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            # csv.DictReader automatically handles quoted fields
            csv_reader = csv.DictReader(csv_file)
            
            # Convert each row to a dictionary, filtering out empty values
            for row in csv_reader:
                # Only include fields that have non-empty values
                filtered_row = {key: value for key, value in row.items() if value and value.strip()}
                locais_coleta.append(filtered_row)
        
        # Create the output structure with version and locaisColeta
        output = {
            "version": int(datetime.now().timestamp()),
            "locaisColeta": locais_coleta
        }
        
        # Write to JSON file
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(output, json_file, indent=2, ensure_ascii=False)
        
        print(f"Successfully converted {csv_file_path} to {json_file_path}")
        print(f"Version: {output['version']}")
        print(f"Total records: {len(locais_coleta)}")
        
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) == 3:
        csv_file = sys.argv[1]
        json_file = sys.argv[2]
    else:
        # Default file names if no arguments provided
        csv_file = "locais.csv"
        json_file = "locais_output.json"
        print(f"Usage: python csv_to_json_custom.py <input.csv> <output.json>")
        print(f"Using default: {csv_file} -> {json_file}")
    
    csv_to_json(csv_file, json_file)