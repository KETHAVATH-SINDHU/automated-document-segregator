# Automated Document Segregator

An automated Python-based tool that analyzes files in a selected folder, identifies their document types based on file extensions, generates visualizations, and optionally organizes files into type-based folders.

## 📌 Project Overview

Managing folders containing different types of documents can be time-consuming. This project automates the process by scanning a folder, identifying file types, displaying a document type summary, generating bar and pie charts, and optionally segregating files into separate folders.

## ✨ Features

- 📂 Scan files from a user-specified folder
- 🔍 Identify document types based on file extensions
- 📊 Display a document type summary
- 📈 Generate a bar chart showing file distribution
- 🥧 Generate a pie chart showing file percentages
- 🗂️ Organize files into type-based folders
- 💾 Save generated charts in an output folder
- 🛡️ Preserve original files by copying them during segregation

## 🛠️ Technologies Used

- Python
- Matplotlib
- OS module
- Shutil module

## 📄 Supported File Types

The program can identify:

- PDF
- DOC / DOCX
- TXT
- CSV
- JPG / JPEG
- PNG
- GIF
- PPT / PPTX
- XLS / XLSX
- PY
- ZIP
- Other file types

## ⚙️ How It Works

1. Enter the path of the folder to analyze.
2. The program scans the files in the folder.
3. Files are classified according to their extensions.
4. A summary of document types is displayed.
5. Bar and pie charts are generated.
6. The charts are saved inside an `output` folder.
7. The user can choose whether to segregate the files.
8. If selected, files are copied into folders based on their document type.
## ▶️ How to Run

### 1. Clone the repository

git clone https://github.com/KETHAVATH-SINDHU/automated-document-segregator.git

### 2. Install the required package

pip install -r requirements.txt

### 3. Run the program

python YOUR_FILE_NAME.py

### 4. Enter the folder path

When prompted, enter the path of the folder you want to analyze.

Example: C:\Users\YourName\Documents\TestFolder
## 📊 Output

The program generates:

- Document type summary in the console
- Bar chart of document distribution
- Pie chart showing document percentages
- Type-based folders when segregation is selected

Generated charts are stored inside the `output` folder.
## 🎯 Project Objective

The main objective of this project is to automate document organization while demonstrating practical applications of:

- File handling
- Python automation
- Data visualization
- Conditional logic
- Directory management

 ## 👩‍💻 Author

**Kethavath Sindhu**

Computer Science and Engineering (Data Science)
