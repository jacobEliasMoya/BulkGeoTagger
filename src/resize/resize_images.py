import os
import io
import zipfile
from PIL import Image

# === USER INPUTS ===
try:
    target_kb = int(input("Enter the target file size in KB (e.g. 500): "))
    if target_kb < 10:
        raise ValueError("Minimum allowed is 10 KB.")
except ValueError as e:
    print(f"❌ Invalid input: {e}")
    exit(1)

convert_to_webp = input("Convert all images to WebP? (y/n): ").strip().lower() == "y"

# === CONFIGURATION ===
MAX_WIDTH = 1920
TARGET_WIDTH = 1280
MIN_QUALITY = 40
INPUT_DIR = "input"
BASE_DIR = INPUT_DIR
OUTPUT_DIR = "output"
SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")


def compress_to_target_size(img, format, target_kb):
    quality = 85
    buffer = io.BytesIO()

    while quality >= MIN_QUALITY:
        buffer.seek(0)
        buffer.truncate()

        img.save(buffer, format=format, optimize=True, quality=quality)
        size_kb = buffer.tell() / 1024

        if size_kb <= target_kb:
            return buffer, quality

        quality -= 5

    return buffer, quality


def resize_and_save(image_path, relative_path):
    img = Image.open(image_path)
    width, height = img.size
    resized = False

    if width > MAX_WIDTH:
        aspect_ratio = height / width
        new_height = int(TARGET_WIDTH * aspect_ratio)
        img = img.resize((TARGET_WIDTH, new_height), Image.LANCZOS)
        resized = True

    # Determine output format and path
    original_format = img.format or image_path.split(".")[-1].upper()
    output_format = "WEBP" if convert_to_webp else original_format

    # Change extension if converting to WebP
    if convert_to_webp:
        relative_path = os.path.splitext(relative_path)[0] + ".webp"

    output_path = os.path.join(OUTPUT_DIR, relative_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if output_format.upper() in ["JPEG", "JPG", "WEBP"]:
        buffer, final_quality = compress_to_target_size(img, output_format, target_kb)
        with open(output_path, "wb") as f:
            f.write(buffer.getvalue())
        msg = f"✅ Resized & Compressed" if resized else "🌀 Compressed only"
        print(f"{msg} → {output_path} (Q{final_quality})")
    else:
        img.save(output_path)
        print(f"🟢 Saved (uncompressed) → {output_path}")


def process_images():
    processed_count = 0
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                full_path = os.path.join(root, file)
                if OUTPUT_DIR in os.path.relpath(full_path, BASE_DIR).split(os.sep):
                    continue
                relative_path = os.path.relpath(full_path, BASE_DIR)
                resize_and_save(full_path, relative_path)
                processed_count += 1
    return processed_count


def zip_output_folder():
    base_name = OUTPUT_DIR
    zip_index = 1
    zip_path = f"{base_name}.zip"

    # Find next available zip filename
    while os.path.exists(zip_path):
        zip_path = f"{base_name}_{zip_index}.zip"
        zip_index += 1

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(OUTPUT_DIR):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, OUTPUT_DIR)
                zipf.write(abs_path, rel_path)

    print(f"\n📦 Created ZIP archive: {zip_path}")


if __name__ == "__main__":
    # Ensure input folder exists
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
        print(f"\n📁 Created 'input/' folder. Add images and run the script again.")
        input("Press Enter to exit...")
        exit()

    count = process_images()
    if count == 0:
        print("\n⚠️ No images needed resizing. Please try again with larger images.")
    else:
        print(f"\n🎉 Done! {count} image(s) processed into '{OUTPUT_DIR}/'")
        zip_output_folder()

    input("\nPress Enter to exit...")
