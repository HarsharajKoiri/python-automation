# 📄 Day 2 - PDF Merger

- This project is a simple PDF Merger built using Python.
- It takes multiple PDF files from a specified folder, merges them into a single PDF (merged-pdf.pdf), and saves the output in the same folder.

# Tech Stack
- PyPDF2 library
- os module


## How It Works
- User provides the folder path where PDF files are stored.
- The program lists all PDFs in the folder.
- It sorts the files alphabetically (optional but keeps it clean).
- Merges all PDFs into one.
- Saves the output as merged-pdf.pdf.
= Prints "PDFs merged successfully!" on success.

## How to Run
- Install the required library:

```bash
pip install PyPDF2
Run the script:
```
```bash
python pdf_merger.py
Enter the path of the folder containing PDF files.
```

## Learnings
- Working with external libraries like PyPDF2.
- Handling file paths and directories.
- Automating repetitive manual tasks.
- Building real-world utility tools.



