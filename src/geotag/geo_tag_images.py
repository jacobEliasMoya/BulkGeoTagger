import json
import os
from PIL import Image
import piexif

def load_city_coords():
    json_files = [f for f in os.listdir() if f.endswith(".json")]

    if not json_files:
        raise FileNotFoundError("No .json file found in this directory.")

    json_path = json_files[0]
    print(f"📄 Using coordinate file: {json_path}")
    
    with open(json_path, "r") as f:
        try:
            data = json.load(f)
            if not isinstance(data, dict) or not data:
                raise ValueError(f"{json_path} is empty or incorrectly formatted.")
            return data
        except json.JSONDecodeError:
            raise ValueError(f"{json_path} contains invalid JSON.")

def to_deg(value, ref_positive, ref_negative):
    ref = ref_positive if value >= 0 else ref_negative
    value = abs(value)
    deg = int(value)
    min_float = (value - deg) * 60
    minutes = int(min_float)
    seconds = int((min_float - minutes) * 60 * 100)
    return ((deg, 1), (minutes, 1), (seconds, 100)), ref

def convert_webp_to_jpg(webp_path):
    jpg_path = webp_path.rsplit('.', 1)[0] + ".jpg"
    with Image.open(webp_path) as img:
        rgb_img = img.convert("RGB")
        rgb_img.save(jpg_path, "JPEG")
    os.remove(webp_path)  # remove the original webp
    print(f"🔄 Converted: {webp_path} → {jpg_path}")
    return jpg_path

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

# Walk through folders and tag images/import from JSON
try:
    city_coords = load_city_coords()
except Exception as e:
    print(f"❌ Error: {e}")
    input("\nPress Enter to exit...")
    exit(1)

tagged_count = 0
checked_folders = 0

for city, coords in city_coords.items():
    folder = f"./{city}"  # assumes unzipped folder is named after city
    if not os.path.isdir(folder):
        continue
    checked_folders += 1
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if file.lower().endswith(".webp"):
            path = convert_webp_to_jpg(path)
            file = os.path.basename(path)  # update filename after conversion
        if file.lower().endswith((".jpg", ".jpeg")):
            add_gps_info(path, *coords)
            print(f"✅ Tagged: {path}")
            tagged_count += 1

if tagged_count == 0:
    if checked_folders == 0:
        print("⚠️  No matching folders found for any cities listed in your .json file.")
    else:
        print("⚠️  No .jpg or .jpeg images found to tag in the available folders.")
else:
    print(f"✅ Done! {tagged_count} image(s) tagged across {checked_folders} folder(s).")

input("\nPress Enter to exit...")
