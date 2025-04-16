# 📍 BulkGeoTagger

**BulkGeoTagger** is a Python-based tool designed to automate the process of geotagging JPEG images based on city-specific folders. It's ideal for photographers, marketers, and SEO professionals who need to embed GPS metadata into images efficiently.

---

## 🚀 Features

- **Automated Geotagging**: Assigns GPS coordinates to images based on their containing folder's city name.
- **Customizable Coordinates**: Utilizes a `city_coords.json` file for flexible city-to-coordinate mappings.
- **Batch Processing**: Handles multiple images across various city folders in one go.
- **Error Handling**: Provides clear warnings if folders or images are missing.

---

## 🗂️ Directory Structure

```
BulkGeoTagger/
├── src/
│   ├── geo_tag_images.py
│   └── city_coords.json
├── dist/
│   └── geo_tag_images.exe
├── releases/
│   └── BulkGeoTagger-Windows.zip
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Usage

### Prerequisites

- Python 3.x
- Required Python packages:
  - `Pillow`
  - `piexif`

Install dependencies:

```bash
pip install Pillow piexif
```

### Running the Script

1. Ensure your `city_coords.json` is populated with the desired city-coordinate mappings.
2. Organize your images into folders named after the cities specified in `city_coords.json`.
3. Execute the script:

```bash
python geo_tag_images.py
```

### Creating an Executable (Optional)

To generate a standalone `.exe` file:

```bash
pyinstaller --onefile geo_tag_images.py
```

The executable will be located in the `dist/` directory.

---

## 📄 city_coords.json Template

```json
{
  "city_name": [latitude, longitude],
  "another_city": [latitude, longitude]
}
```

**Example:**

```json
{
  "phoenix": [33.4484, -112.0740],
  "mesa": [33.4152, -111.8315]
}
```

---

## 🧪 Example Usage

Given the following structure:

```
BulkGeoTagger/
├── phoenix/
│   └── image1.jpg
├── mesa/
│   └── image2.jpg
├── city_coords.json
└── geo_tag_images.py
```

Running the script will geotag `image1.jpg` and `image2.jpg` with the coordinates specified for Phoenix and Mesa, respectively.

---

## 🛠️ Troubleshooting

- **No Matching Folders**: Ensure that the folder names match the keys in `city_coords.json`.
- **No Images Found**: Confirm that the folders contain `.jpg` or `.jpeg` files.
- **Invalid JSON**: Validate the syntax of your `city_coords.json` file.

---

## 📬 Feedback & Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/jacobEliasMoya/BulkGeoTagger/issues).

---

## 👤 Author

Created and maintained by [Jacob Elias Moya](https://github.com/jacobEliasMoya)  
If you use this tool or build upon it, let me know — I’d love to see what you create.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
