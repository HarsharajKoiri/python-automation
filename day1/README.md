# File Organizer Script

This Python script automatically organizes files in a folder based on their extensions. It categorizes the files into specific folders like Images, Documents, Audio, Video, Archives, and others, making it easy to manage large numbers of files.

## Features

- Categorizes files into the following folders:
  - **Images** (e.g., jpg, jpeg, png, gif, bmp)
  - **Documents** (e.g., txt, pdf, doc, docx, odt)
  - **Archives** (e.g., zip, tar, rar, 7z, gz)
  - **Audio** (e.g., mp3, wav, flac)
  - **Videos** (e.g., mp4, mkv, avi, mov)
  - **Others** (for files that do not match any of the above extensions)
  
- Creates new folders for each category if they do not exist.
- Renames files if a file with the same name already exists in the target folder to avoid overwriting.
  
## Requirements

- Python 3.x
- Libraries: `os`, `shutil`, `collections`

## Usage

1. Clone or download this repository.
2. Run the script using the following command:

   ```bash
   python file_organizer.py


## Input:

  ```bash
  Enter the full path of the folder you want to organize: /path/to/your/folder
  ```

## Output:

  ```bash
  Found 10 items in the folder.

  Moved: image1.jpg ➝ /path/to/your/folder/Images
  Moved: document1.pdf ➝ /path/to/your/folder/Documents
  Moved: song.mp3 ➝ /path/to/your/folder/Audio
  ```

## Notes
- The script uses extensions to categorize the files. If a file doesn't match any of the predefined categories, it will be moved to the
  "Others" folder.

- Files with the same name in the target folder will be renamed to avoid conflicts (e.g., file_1.jpg).
