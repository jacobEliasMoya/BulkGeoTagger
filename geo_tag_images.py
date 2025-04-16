
import os
from PIL import Image
import piexif

# Predefined coordinates
city_coords = {
    "menifee": (33.6971, -117.1853),
    "loomis": (38.8216, -121.1930),
    "colfax": (39.1005, -120.9530),
    "rocklin": (38.7907, -121.2358),
    "lincoln": (38.8916, -121.2930),
    "roseville": (38.7521, -121.2880)
}

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

# Walk through folders and tag images
for city, coords in city_coords.items():
    folder = f"./{city}"  # assumes unzipped folder is named after city
    if not os.path.isdir(folder):
        continue
    for file in os.listdir(folder):
        if file.lower().endswith((".jpg", ".jpeg")):
            path = os.path.join(folder, file)
            add_gps_info(path, *coords)
            print(f"Tagged: {path}")
