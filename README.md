# 🛠️ ProductivePyton

**ProductivePyton** is a suite of lightweight command-line tools for bulk image processing and optimization. It includes:

- 📍 **BulkGeoTagger** — Geotags images by folder-based city names using embedded GPS metadata.
- 📷 **BulkCompressor** — Compresses, resizes, and optionally converts images to WebP format with target file size control.

---

## 📁 Tools Included

### 📍 BulkGeoTagger

**Auto-tag your images by location.**

**Usage:**

1. Add folders named after cities (e.g. `phoenix`, `mesa`)
2. Make sure `city_coords.json` matches folder names:

```json
{
  "phoenix": [33.4484, -112.0740],
  "mesa": [33.4152, -111.8315]
}
```

3. Run:
```bash
python geo_tag_images.py
```
Or use the prebuilt `.exe` (Windows only).

📂 Your image structure should look like:

```
/phoenix/photo1.jpg
/mesa/photo2.jpg
```

---

### 📷 BulkCompressor

**Resize, compress, and optionally convert images to WebP.**

**Features:**

- Resizes images wider than 1920px
- Compresses to a user-defined file size
- Optional `.webp` conversion
- Zips final output

**Usage:**

```bash
python resize_images.py
```

You’ll be prompted for:

- Desired file size in KB
- WebP conversion option

Input images must go in the `/input` directory. Output is saved to `/output`.

---

## 💾 Folder Structure

```
ProductivePyton/
├── src/
│   ├── geotag/
│   │   ├── geo_tag_images.py
│   │   ├── city_coords.json
│   ├── resize/
│   │   └── resize_images.py
├── dist/                        # Windows executables
├── releases/                   # Zip release bundles
```

---

## 📦 Dependencies

Install required Python packages:

```bash
pip install Pillow piexif
```

---

## 👤 Author

Made by [Jacob Elias Moya](https://github.com/jacobEliasMoya)  
Built for efficient image prep at scale.

---

## 📄 License

MIT License — free to use, modify, and distribute.
