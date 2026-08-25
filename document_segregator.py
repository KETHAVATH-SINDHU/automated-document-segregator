"""
Automated Document Segregator with Document Type Analysis
and Data Visualization using Python

Built using only Python's built-in modules (os, shutil) and matplotlib.
Developed and tested in Spyder IDE, Notepad, and Windows CMD.
"""

import os
import shutil
import matplotlib.pyplot as plt


# ---------------------------------------------------------------
# Extension-to-document-type mapping
# ---------------------------------------------------------------
document_type_map = {
    ".pdf": "PDF",
    ".doc": "DOC",
    ".docx": "DOCX",
    ".txt": "TXT",
    ".csv": "CSV",
    ".jpg": "JPG",
    ".jpeg": "JPG",
    ".png": "PNG",
    ".gif": "GIF",
    ".ppt": "PPT",
    ".pptx": "PPTX",
    ".xls": "XLS",
    ".xlsx": "XLSX",
    ".py": "PY",
    ".zip": "ZIP",
}


def get_document_type(file_name):
    """Return the document type label for a given file name."""
    _, extension = os.path.splitext(file_name)
    extension = extension.lower()
    return document_type_map.get(extension, "OTHERS")


def scan_folder(folder_path):
    """Scan folder_path and return (file_names, type_counts)."""
    file_names = os.listdir(folder_path)
    type_counts = {}

    for file_name in file_names:
        doc_type = get_document_type(file_name)
        if doc_type in type_counts:
            type_counts[doc_type] = type_counts[doc_type] + 1
        else:
            type_counts[doc_type] = 1

    return file_names, type_counts


def print_summary(type_counts):
    """Print the document type counts to the console."""
    print("\nDocument Type Summary")
    print("-" * 30)
    for doc_type, count in type_counts.items():
        print(f"{doc_type:<10}: {count}")
    print("-" * 30)


def plot_bar_chart(type_counts, output_path):
    """Generate and save a bar chart of document type counts."""
    types = list(type_counts.keys())
    counts = list(type_counts.values())

    plt.figure(figsize=(8, 5))
    plt.bar(types, counts, color="steelblue")
    plt.xlabel("Document Type")
    plt.ylabel("Number of Files")
    plt.title("Document Type Distribution - Bar Chart")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, facecolor="white")
    plt.close()


def plot_pie_chart(type_counts, output_path):
    """Generate and save a pie chart of document type percentages."""
    types = list(type_counts.keys())
    counts = list(type_counts.values())

    plt.figure(figsize=(7, 7))
    plt.pie(counts, labels=types, autopct="%1.1f%%", startangle=90)
    plt.title("Document Type Distribution - Pie Chart")
    plt.axis("equal")
    plt.savefig(output_path, dpi=150, facecolor="white")
    plt.close()


def segregate_files(folder_path, file_names):
    """Copy each file into a sub-folder named after its document type."""
    for file_name in file_names:
        doc_type = get_document_type(file_name)
        destination_folder = os.path.join(folder_path, doc_type)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        source_path = os.path.join(folder_path, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)


def main():
    folder_path = input("Enter the folder path to analyze: ").strip()

    if not os.path.exists(folder_path):
        print("Error: The specified folder path does not exist.")
        return

    file_names, type_counts = scan_folder(folder_path)

    if not file_names:
        print("No files found in the specified folder.")
        return

    print_summary(type_counts)

    output_folder = os.path.join(folder_path, "output")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    plot_bar_chart(type_counts, os.path.join(output_folder, "bar_chart.jpg"))
    plot_pie_chart(type_counts, os.path.join(output_folder, "pie_chart.jpg"))
    print("Bar chart and pie chart saved in the 'output' folder.")

    choice = input(
        "Do you want to segregate files into type folders? (yes/no): "
    ).strip().lower()
    if choice == "yes":
        segregate_files(folder_path, file_names)
        print("Files segregated successfully into extension-based folders.")
    else:
        print("Segregation skipped. Original folder left unchanged.")


if __name__ == "__main__":
    main()
