import os
import shutil

folder_path = "C:\\Users\\Harshi_symnn\\Downloads"

files = os.listdir(folder_path)

# Folder names
image_folder = os.path.join(folder_path, "Images")
pdf_folder = os.path.join(folder_path, "Documents")
app_folder = os.path.join(folder_path, "Applications")

# Create folders if they don't exist
os.makedirs(image_folder, exist_ok=True)
os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(app_folder, exist_ok=True)

for file in files:

    if os.path.isdir(os.path.join(folder_path, file)):
        continue
        
    source = os.path.join(folder_path, file)

    if file.endswith(".jpg"):
        shutil.move(source, image_folder)
        print(f"Moved {file} to Images")

    elif file.endswith(".pdf"):
        shutil.move(source, pdf_folder)
        print(f"Moved {file} to Documents")

    elif file.endswith(".exe"):
        shutil.move(source, app_folder)
        print(f"Moved {file} to Applications")