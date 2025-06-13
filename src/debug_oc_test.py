import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_path = r'D:\ocr_assignment\data\images\Application_055918284page1.png'
img = cv2.imread(img_path)

if img is None:
    print("Error: Image not found or corrupted.")
    exit()

# 1. Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Apply OTSU thresholding
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 3. (Optional) Denoise
denoised = cv2.fastNlMeansDenoising(thresh, h=30)

# 4. OCR on preprocessed image
text = pytesseract.image_to_string(denoised)

print("\n--- OCR OUTPUT ---\n")
print(text)


