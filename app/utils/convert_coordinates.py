import json

# Read the JSON file
with open('locations_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert lat and lng from strings to floats
for location in data['locaisColeta']:
    location['lat'] = float(location['lat'])
    location['lng'] = float(location['lng'])

# Write the updated data back to the file
with open('locations_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print(f"Converted {len(data['locaisColeta'])} locations successfully!")