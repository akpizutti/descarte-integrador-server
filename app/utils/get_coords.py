import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time
import argparse
import sys

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) # print a message in red

def get_coordinates(address, geolocator, max_retries=3):
    """
    Get coordinates for an address with retry logic.
    Returns tuple (latitude, longitude) or (None, None) if failed.
    """
    for attempt in range(max_retries):
        try:
            location = geolocator.geocode(address, timeout=10)
            if location:
                return location.latitude, location.longitude
            else:
                return None, None
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            if attempt < max_retries - 1:
                time.sleep(1)  # Wait before retry
                continue
            else:
                print(f"Error geocoding '{address}': {e}")
                return None, None

def has_coordinates(lat, long):
    """Check if both lat and long have valid values"""
    return (pd.notna(lat) and pd.notna(long) and 
            lat != '' and long != '' and 
            lat != 'None' and long != 'None')

def process_addresses(input_file, output_file, city="Porto Alegre, RS, Brazil"):
    """
    Read CSV, geocode addresses, and save results.
    """
    # Read CSV file
    df = pd.read_csv(input_file, keep_default_na=True, na_values=['', 'NA', 'NaN', 'None'])
    
    # Initialize geolocator (using Nominatim - free OpenStreetMap service)
    geolocator = Nominatim(user_agent="address_geocoder")
    
    # Create lat/long columns if they don't exist
    if 'lat' not in df.columns:
        df['lat'] = None
    if 'long' not in df.columns:
        df['long'] = None
    
    # Process each address
    total = len(df)
    success_count = 0
    failed_count = 0
    skipped_count = 0
    
    for index, row in df.iterrows():
        street_address = row['endereco']
        
        # Skip if already has coordinates
        if has_coordinates(row['lat'], row['long']):
            print(f"[{index+1}/{total}] Skipping (already has coords): {street_address} (lat={row['lat']}, long={row['long']})")
            skipped_count += 1
            continue
        
        # Add city information to the address
        full_address = f"{street_address}, {city}"
        
        print(f"[{index+1}/{total}] Processing: {full_address}")
        
        lat, long = get_coordinates(full_address, geolocator)
        df.at[index, 'lat'] = lat
        df.at[index, 'long'] = long
        
        # Print results
        if lat is not None and long is not None:
            print(f"SUCCESS: Latitude={lat}, Longitude={long}")
            success_count += 1
        else:
            prRed(f"WARNING: Could not find coordinates for '{street_address}'")
            failed_count += 1
        
        # Be respectful to the free service - add delay between requests
        time.sleep(1)
    
    # Save results
    df.to_csv(output_file, index=False)
    print(f"\n{'='*60}")
    print(f"Completed! Results saved to {output_file}")
    print(f"Skipped (already had coords): {skipped_count}")
    print(f"Successful geocodes: {success_count}")
    print(f"Failed geocodes: {failed_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Geocode addresses from CSV file')
    parser.add_argument('input_file', help='Input CSV file path')
    parser.add_argument('-o', '--output', help='Output CSV file path (default: adds _geocoded to input filename)')
    parser.add_argument('-c', '--city', default='Porto Alegre, RS, Brazil', 
                       help='City/region to append to addresses (default: Porto Alegre, RS, Brazil)')
    
    args = parser.parse_args()
    
    # Generate output filename if not provided
    if args.output:
        output_file = args.output
    else:
        # Add _geocoded before the extension
        if args.input_file.endswith('.csv'):
            output_file = args.input_file[:-4] + '_geocoded.csv'
        else:
            output_file = args.input_file + '_geocoded.csv'
    
    process_addresses(args.input_file, output_file, args.city)