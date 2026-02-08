import re
import os

file_path = 'products.html'
# specific images to NOT start with images/products if they are outside
# target specific pattern: src="images/products/... .png|.jpg"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find src="images/products/..." ending in .png or .jpg
    # Capture group 1 is the prefix up to the extension
    # We replace with \1.webp"
    # Case insensitive for extensions? Usually lowercase in this project but let's be safe-ish for the regex
    
    # Pattern: src="images/products/path/to/image.png"
    pattern = r'(src=["\']images/products/[^"\']+)\.(png|jpg)(["\'])'
    
    def replacement(match):
        return f'{match.group(1)}.webp{match.group(3)}'

    new_content, count = re.subn(pattern, replacement, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Updated {count} image references to WebP.")

except Exception as e:
    print(f"Error: {e}")
