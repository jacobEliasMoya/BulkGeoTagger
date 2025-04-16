# run.py
# Example usage of BulkGeoTagger // not for production

import os
from src.geo_tag_images import load_city_coords, add_gps_info

if __name__ == "__main__":
    # Path setup
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "src", "city_coords.json")

    # Load coordinates
    try:
        city_coords = load_city_coords(json_path)
    except Exception as e:
        print(f"Failed to load city coordinates: {e}")
        exit(1)

    # Dummy walk through folders (for example only)
    for city, coords in city_coords.items():
        folder = os.path.join(current_dir, "src", city)
        if os.path.isdir(folder):
            print(f"Would tag images in: {folder} with {coords}")
        else:
            print(f"Missing folder: {folder}")
