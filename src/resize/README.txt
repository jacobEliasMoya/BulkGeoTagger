# 📷 Bulk Image Compressor & Optimizer

This CLI tool automates the compression, resizing, WebP conversion, and zip packaging of large image batches.

Ideal for devs and creatives who need quick, consistent output — especially when working with assets that must be optimized for performance or delivery.

---
## 🧑‍💻 Usage

1. **Drop your images into the `input/` folder**

2. **Run the script in your termial:**

```
cd Desktop\pytools\src\resize\; python resize_images.py
```

3. **You'll be prompted to:**
   - Set the target file size in KB (e.g. `400`)
   - Choose whether to convert all images to WebP (`y/n`)

4. **Results:**
   - Optimized images are saved to `output/`
   - A zip archive (e.g., `output.zip`, `output_1.zip`) is created
   - Original images in `input/` remain untouched

---
---

## 🚀 Features

- 🔻 Resize images wider than 1920px (maintains aspect ratio)
- 📦 Compress images to a user-defined target file size (in KB)
- 🌐 Optional WebP conversion
- 🗂️ Preserves input folder structure
- 🧼 Outputs to `output/` folder
- 🧳 Auto-creates a zip archive of the processed results

---

## 🛠️ Requirements

- Python 3.7+
- Pillow (`pip install pillow`)

---

## 📁 Folder Structure

```
project/
│
├── input/          # Put your raw .jpg/.png/.webp images here
├── output/         # Processed results go here
├── output.zip      # Auto-created zip of the output folder
└── image_tool.py   # This script
```

---



## 🧠 How It Works

- Resizes any image wider than 1920px to 1280px wide, keeping the original aspect ratio
- Compresses JPEG and WebP images to your specified KB target using smart quality reduction
- Converts to WebP if chosen
- Non-JPEG/WebP formats (e.g., PNG) are saved as-is unless converted

---

## ⚠️ Notes

- Images already below the size/width target are still copied and compressed
- Zip filenames auto-increment to avoid overwriting previous runs
- Input and output folders are created automatically if missing

---

## ✅ Supported Formats

- `.jpg`
- `.jpeg`
- `.png`
- `.webp`

---

## 📬 Questions or Improvements?

Feel free to tweak the config section of the script to change:
- Max width (`MAX_WIDTH`)
- Target width (`TARGET_WIDTH`)
- Minimum compression quality (`MIN_QUALITY`)

---

Built with speed and sanity in mind ✌️
