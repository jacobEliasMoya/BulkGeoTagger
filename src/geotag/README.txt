📦 BulkGeoTagger - Windows Release
----------------------------------

🟢 HOW TO USE:
1. Place your images in folders named after cities (e.g., "phoenix", "mesa")
2. Ensure those city names match the keys in city_coords.json
3. Double-click "geo_tag_images.exe"

The app will:
✔️ Auto-load city_coords.json
✔️ Look for folders named after cities
✔️ Geotag all .jpg/.jpeg images inside

📝 EXAMPLE:
- city_coords.json includes:
  {
    "phoenix": [33.4484, -112.0740]
  }

- Your folder should look like:
  BulkGeoTagger/
  ├── geo_tag_images.exe
  ├── city_coords.json
  └── phoenix/
      └── yourimage.jpg

⚠️ If no folders/images are found, the tool will warn you.

🧠 Tip: All folders and city names must be lowercase and match exactly.

Made by jacobEliasMoya
https://github.com/jacobEliasMoya/BulkGeoTagger
