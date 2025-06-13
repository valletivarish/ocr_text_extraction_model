# import os
# from pdf2image import convert_from_path
# import pytesseract
# import cv2

# # Hardcoded paths
# PDF_INPUT_DIR = r"D:\ocr_assignment\data\raw_pdfs"
# IMAGE_OUTPUT_DIR = r"D:\ocr_assignment\data\images"
# TEXT_OUTPUT_DIR = r"D:\ocr_assignment\data\ocr_text"

# # Tesseract installation path
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# def convert_pdf_to_images(pdf_path, output_folder):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#     images = convert_from_path(pdf_path)
#     image_paths = []
#     base_name = os.path.splitext(os.path.basename(pdf_path))[0]
#     for i, image in enumerate(images):
#         image_path = os.path.join(output_folder, f"{base_name}_page{i + 1}.png")
#         image.save(image_path, "PNG")
#         image_paths.append(image_path)
#     return image_paths

# def ocr_image(image_path):
#     img = cv2.imread(image_path)
#     if img is None:
#         print(f"❌ Error reading image: {image_path}")
#         return ""

#     # Preprocessing: grayscale → OTSU threshold → denoise
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#     denoised = cv2.fastNlMeansDenoising(thresh, h=30)

#     # OCR
#     return pytesseract.image_to_string(denoised)

# def extract_text_from_pdf(pdf_path):
#     base_name = os.path.splitext(os.path.basename(pdf_path))[0]
#     image_output_subdir = os.path.join(IMAGE_OUTPUT_DIR, base_name)
#     image_paths = convert_pdf_to_images(pdf_path, image_output_subdir)

#     full_text = ""
#     for img_path in image_paths:
#         print(f"🔍 OCR on: {img_path}")
#         text = ocr_image(img_path)
#         full_text += text + "\n"

#     text_output_file = os.path.join(TEXT_OUTPUT_DIR, f"{base_name}.txt")
#     with open(text_output_file, "w", encoding="utf-8") as f:
#         f.write(full_text)

#     print(f"✅ OCR done for: {pdf_path}")
#     print(f"📄 Output saved to: {text_output_file}")

# def process_all_pdfs():
#     if not os.path.exists(TEXT_OUTPUT_DIR):
#         os.makedirs(TEXT_OUTPUT_DIR)

#     pdf_files = [f for f in os.listdir(PDF_INPUT_DIR) if f.lower().endswith(".pdf")]

#     if not pdf_files:
#         print("⚠ No PDFs found to process.")
#         return

#     for pdf_file in pdf_files:
#         pdf_path = os.path.join(PDF_INPUT_DIR, pdf_file)
#         extract_text_from_pdf(pdf_path)

# if __name__ == "__main__":
#     process_all_pdfs()

