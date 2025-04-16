# 📸 BulkGeoTagger

BulkGeoTagger is a simple Python script that applies geolocation metadata (latitude and longitude) to JPEG images based on folder names and a central city coordinate mapping. It’s ideal for SEO, content automation, and photography workflows.

---

## 🧠 How It Works

The script reads a file called `city_coords.json`, which contains a list of cities and their coordinates. It searches for folders named after those cities and geotags any `.jpg` or `.jpeg` images inside them using GPS metadata.

---

## 📁 File & Folder Structure

```
BulkGeoTagger/
├── geo_tag_images.py         # Main script
├── city_coords.json          # List of city coordinates
└── ...
```

---

## 🧾 Example `city_coords.json`

```json
{
    "phoenix": [33.4484, -112.0740],
    "sun_city": [33.4942, -111.9261]
}
```

- Keys must be lowercase and use underscores instead of spaces (e.g., `sun_city`)
- Values must be arrays of two floats: `[latitude, longitude]`

--- 

## 🚀 Usage

1. Clone or download this repository
2. Add your images into folders named after the cities in `city_coords.json`
3. From the root directory, run:

```bash
python geo_tag_images.py
```

The script will:
- Automatically load `city_coords.json`
- Walk through folders
- Apply geotags to matching `.jpg` or `.jpeg` files

---

## 💡 Use Cases

- SEO optimization for local content  
- Location-based photo tagging  
- Automating alt-text or Google Maps integration

---

## 👤 Author

Made by [jacobEliasMoya](https://github.com/jacobEliasMoya) 
Open to contributions and feedback — PRs welcome!
