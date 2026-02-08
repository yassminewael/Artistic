import os
from PIL import Image

def convert_to_webp(root_dir):
    print(f"Scanning {root_dir}...")
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            filename, ext = os.path.splitext(file)
            ext = ext.lower()
            
            if ext in ['.png', '.jpg', '.jpeg']:
                target_path = os.path.join(subdir, filename + ".webp")
                
                # Skip if webp already exists and is newer
                if os.path.exists(target_path):
                   continue
                
                try:
                    with Image.open(file_path) as img:
                        print(f"Converting {file} to WebP...")
                        img.save(target_path, "WEBP", quality=85)
                except Exception as e:
                    print(f"Failed to convert {file}: {e}")

if __name__ == "__main__":
    # Adjust path if needed, assuming running from project root
    images_dir = os.path.join(os.getcwd(), "images", "products")
    if os.path.exists(images_dir):
        convert_to_webp(images_dir)
    else:
        print(f"Directory not found: {images_dir}")
