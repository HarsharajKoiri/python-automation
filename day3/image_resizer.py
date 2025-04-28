from PIL import Image
import os

# Step 1: Take input
source_folder = input("Enter the path to the folder containing images: ")
output_folder = os.path.join(source_folder, "resized-images")

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Step 2: Desired size
new_width = int(input("Enter new width: "))
new_height = int(input("Enter new height: "))

# Step 3: Resize all images
for filename in os.listdir(source_folder):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(source_folder, filename)
        img = Image.open(img_path)
        resized_img = img.resize((new_width, new_height))
        
        save_path = os.path.join(output_folder, filename)
        resized_img.save(save_path)

print(f"✅ All images resized and saved to '{output_folder}'!")
