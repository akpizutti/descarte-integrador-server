import json
import os

class CollectionService:
    def __init__(self, data_file='app/utils/locations_data.json'):
        self.data_file = data_file
        self.locations = self.load_locations()

    def _empty_data(self):
        return {"version": 0, "locaisColeta": []}

    def load_locations(self):
        if not os.path.exists(self.data_file):
            print(f"WARNING: JSON database file not found at '{self.data_file}'")
            print("WARNING: Server will start with empty location data.")
            return self._empty_data()

        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(f"SUCCESS: Loaded {len(data.get('locaisColeta', []))} locations from '{self.data_file}'")
                return data
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON format in '{self.data_file}': {e}")
        except Exception as e:
            print(f"ERROR: Failed to load '{self.data_file}': {e}")

        return self._empty_data()

    def get_locations(self):
        return self.locations.get('locaisColeta', [])

    def get_version(self):
        return {"version": self.locations.get('version', 0)}