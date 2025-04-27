import PyPDF2
import os

# Take folder path input from user
folder_path = input("Enter the folder path where PDFs are stored: ")

# Change working directory to the folder
os.chdir(folder_path)

# Get list of PDFs
pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]
pdf_files.sort()

# Merge PDFs
merger = PyPDF2.PdfMerger()

for pdf in pdf_files:
    merger.append(pdf)

# Save the final merged PDF
output_path = os.path.join(folder_path, 'merged_output.pdf')
merger.write(output_path)
merger.close()

print(f"All PDFs merged successfully into '{output_path}' 🎉")
