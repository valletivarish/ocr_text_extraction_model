from pdf_to_text import extract_text_from_pdf
import os

pdf_name = "Application_055918284.pdf"  # 👈 replace with actual PDF file name
pdf_path = os.path.join("..", "data", "raw_pdfs", pdf_name)
image_dir = os.path.join("..", "data", "images")
text_output = os.path.join("..", "data", "ocr_text", pdf_name.replace(".pdf", ".txt"))

extract_text_from_pdf(pdf_path, image_dir, text_output)