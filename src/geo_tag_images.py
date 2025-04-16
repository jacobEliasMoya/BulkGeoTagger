import json
import os
from PIL import Image
import piexif

def load_city_coords(json_path="city_coords.json"):
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"City coordinates file not found: {json_path}")
    
    with open(json_path, "r") as f:
        try:
            data = json.load(f)
            if not isinstance(data, dict) or not data:
                raise ValueError("city_coords.json is empty or incorrectly formatted.")
            return data
        except json.JSONDecodeError:
            raise ValueError("city_coords.json contains invalid JSON.")

def to_deg(value, ref_positive, ref_negative):
    ref = ref_positive if value >= 0 else ref_negative
    value = abs(value)
    deg = int(value)
    min_float = (value - deg) * 60
    minutes = int(min_float)
    seconds = int((min_float - minutes) * 60 * 100)
    return ((deg, 1), (minutes, 1), (seconds, 100)), ref

def add_gps_info(image_path, lat, lon):
    img = Image.open(image_path)
    exif_bytes = img.info.get('exif')
    exif_dict = piexif.load(exif_bytes) if exif_bytes else {"0th":{}, "Exif":{}, "GPS":{}, "1st":{}, "thumbnail": None}
    lat_dms, lat_ref = to_deg(lat, "N", "S")
    lon_dms, lon_ref = to_deg(lon, "E", "W")
    gps_ifd = {
        piexif.GPSIFD.GPSLatitudeRef: lat_ref.encode(),
        piexif.GPSIFD.GPSLatitude: lat_dms,
        piexif.GPSIFD.GPSLongitudeRef: lon_ref.encode(),
        piexif.GPSIFD.GPSLongitude: lon_dms,
    }
    exif_dict['GPS'] = gps_ifd
    exif_bytes = piexif.dump(exif_dict)
    img.save(image_path, "jpeg", exif=exif_bytes)

# Walk through folders and tag images/ importing from json
try:
    city_coords = load_city_coords()
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

tagged_count = 0
checked_folders = 0

for city, coords in city_coords.items():
    folder = f"./{city}"  # assumes unzipped folder is named after city
    if not os.path.isdir(folder):
        continue
    checked_folders += 1
    for file in os.listdir(folder):
        if file.lower().endswith((".jpg", ".jpeg")):
            path = os.path.join(folder, file)
            add_gps_info(path, *coords)
            print(f"✅ Tagged: {path}")
            tagged_count += 1

if tagged_count == 0:
    if checked_folders == 0:
        print("⚠️  No matching folders found for any cities listed in city_coords.json.")
    else:
        print("⚠️  No .jpg or .jpeg images found to tag in the available folders.")
else:
    print(f"✅ Done! {tagged_count} image(s) tagged across {checked_folders} folder(s).")