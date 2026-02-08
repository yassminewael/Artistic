import os
import glob

# Define the root directory to search
root_dir = 'images'

extensions_to_delete = ['.png', '.jpg', '.jpeg']

deleted_count = 0
skipped_count = 0

for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_path = os.path.join(root, file)
        base_name, ext = os.path.splitext(file_path)
        
        if ext.lower() in extensions_to_delete:
            # Check if .webp version exists
            webp_path = base_name + '.webp'
            if os.path.exists(webp_path):
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    deleted_count += 1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
            else:
                print(f"Skipped (no WebP found): {file_path}")
                skipped_count += 1

print(f"\nCleanup complete.")
print(f"Total deleted: {deleted_count}")
print(f"Total skipped: {skipped_count}")
