import os
import csv
import pdf2image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Programs\Tesseract-OCR\tesseract.exe'

def read_pdf_invoice(file_path):
    # Convert PDF pages to images
    images = pdf2image.convert_from_path(file_path)

    invoice_text = ""
    for image in images:
        # Perform OCR on each image
        text = pytesseract.image_to_string(image, lang="lav", config='--psm 6')
        invoice_text += text
    
    start_text = "-------- Elektroniska izdruka ---------"
    end_text = "Apmaksa"
    
    start_index = invoice_text.find(start_text) + len(start_text)
    end_index = invoice_text.index(end_text)

    desired_text = invoice_text[start_index:end_index].strip()
    desired_text = desired_text.replace("Depozita maksa", "")
    
    return desired_text

# Path to the data folder
data_folder = "data"

# Initialize the CSV file
csv_file_path = "invoices.csv"
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['File Name', 'Invoice Text'])

    # Iterate over files in the data folder
    for filename in os.listdir(data_folder):
        # Construct the file path
        file_path = os.path.join(data_folder, filename)

        # Read the invoice
        invoice_text = read_pdf_invoice(file_path)

        # Write the file name and extracted text to the CSV file
        writer.writerow([filename, invoice_text])

print("CSV file has been created: invoices.csv")
