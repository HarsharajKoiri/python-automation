import os
import shutil
from collections import defaultdict

# Function to categorize file extensions
def categorize_file(file_ext):
    image_ext = ['jpg', 'jpeg', 'png', 'gif', 'bmp']
    document_ext = ['txt', 'pdf', 'doc', 'docx', 'odt']
    archive_ext = ['zip', 'tar', 'rar', '7z', 'gz']
    audio_ext = ['mp3', 'wav', 'flac']
    video_ext = ['mp4', 'mkv', 'avi', 'mov']

    if file_ext.lower() in image_ext:
        return 'Images'
    elif file_ext.lower() in document_ext:
        return 'Documents'
    elif file_ext.lower() in archive_ext:
        return 'Archives'
    elif file_ext.lower() in audio_ext:
        return 'Audio'
    elif file_ext.lower() in video_ext:
        return 'Videos'
    else:
        return 'Others'

# Input folder path
folder_path = input("Enter the full path of the folder you want to organize: ")

if not os.path.exists(folder_path):
    print("The folder path you entered does not exist. Please check and try again.")
    exit()

files = os.listdir(folder_path)
print(f"\nFound {len(files)} items in the folder.\n")

# Dictionary to track the folders and the number of files moved
folder_status = defaultdict(int)
moved_files = []

for file in files:
    file_path = os.path.join(folder_path, file)
    
    if os.path.isfile(file_path):
        # Handle file extension
        file_ext = file.split('.')[-1] if '.' in file else 'no_extension'
        
        # Categorize file into appropriate folder
        category_folder = categorize_file(file_ext)
        target_folder = os.path.join(folder_path, category_folder)
        
        # Create category folder if not exist
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        
        # Avoid overwriting by renaming the file if needed
        target_file_path = os.path.join(target_folder, file)
        if os.path.exists(target_file_path):
            base, ext = os.path.splitext(file)
            count = 1
            while os.path.exists(target_file_path):
                target_file_path = os.path.join(target_folder, f"{base}_{count}{ext}")
                count += 1

        # Move the file
        shutil.move(file_path, target_file_path)
        moved_files.append(file)
        folder_status[category_folder] += 1
        print(f"Moved: {file} ➝ {target_folder}")

# Summary
print("\nSummary:")
for category, count in folder_status.items():
    print(f"{category}: {count} files moved.")

if moved_files:
    print(f"\nTotal {len(moved_files)} files were organized.")
else:
    print("\nNo files were moved.")
