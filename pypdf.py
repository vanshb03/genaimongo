import os
import PyPDF2
import json

def pdf_to_json_text(pdf_file):
  """
  Extracts text from a PDF and stores it in a dictionary

  Args:
      pdf_file (str): Path to the PDF file

  Returns:
      dict: Dictionary containing extracted text data
  """
  pdf_reader = PyPDF2.PdfReader(pdf_file)
  text_data = {}

  for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text_data[f"Page {page_num+1}"] = page.extract_text()

  return text_data

def convert_folder_to_json(folder_path):
  """
  Iterates through all PDFs in a folder and converts them to JSON files

  Args:
      folder_path (str): Path to the folder containing PDFs
  """
  for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
      pdf_path = os.path.join(folder_path, filename)
      text_data = pdf_to_json_text(pdf_path)

      # Generate unique JSON filename (optional)
      json_filename = os.path.splitext(filename)[0] + ".json"  

      with open(os.path.join(folder_path, json_filename), "w") as outfile:
        json.dump(text_data, outfile)

# Replace with the actual path to your folder containing PDFs
folder_path = "manuals"
convert_folder_to_json(folder_path)
