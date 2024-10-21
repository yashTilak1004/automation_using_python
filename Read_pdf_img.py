'''
from pdfquery import PDFQuery

pdf = PDFQuery('ANY900648244.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

print(text)
'''
'''
from PyPDF2 import PdfReader

pdf_document = input("file: ")

file_name = pdf_document.split('.')

text_file = f'{file_name[0]}.txt'

with open(pdf_document, "rb") as filehandle, open(text_file, mode='w', encoding='UTF-8') as output:
    pdf = PdfReader(filehandle)
    num_of_pages = len(pdf.pages)
    for page_number in range(num_of_pages):
        page = pdf.pages[page_number]
        print(f"Page: {page_number+1}", file=output)
        print('', file=output)
        print(page.extract_text(), file=output)
        print('', file=output)
'''
'''
from PyPDF2 import PdfReader

reader = PdfReader("first.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)
'''
'''
from pdfminer.high_level import extract_text  
text = extract_text("first.pdf") # <== Give your pdf name and path.  
print(text)
'''
'''
from PIL import Image
 
# Read image
img = Image.open("C:\\Users\\Yashwanth.Akuthota\\Pictures\\Screenshots\\Screenshot 2024-10-03 143251.png")
 
# Output Images
img.show()
 
# prints format of image
print(img.format)
 
# prints mode of image
print(img.mode)
'''



#reading images through pytesseract
'''
from PIL import Image 
from pytesseract import pytesseract 
  
# Defining paths to tesseract.exe 
# and the image we would be using 
path_to_tesseract = r"C:\\Users\\Yashwanth.Akuthota\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
image_path = r"C:\\Users\\Yashwanth.Akuthota\\Pictures\\Screenshots\\Screenshot 2024-10-03 143251.png"

# Opening the image & storing it in an image object 
img = Image.open(image_path) 
  
# Providing the tesseract executable 
# location to pytesseract library 
pytesseract.tesseract_cmd = path_to_tesseract 
  
# Passing the image object to image_to_string() function 
# This function will extract the text from the image 
text = pytesseract.image_to_string(img) 
  
# Displaying the extracted text 
print(text[:-1])
'''

#612 and 792-> 8.5 and 11 inches
#find length of a page in python
'''
import fitz  # PyMuPDF
# Open the PDF file
pdf_document = fitz.open("your_file.pdf")
# Select the first page
page = pdf_document[0]
# Get the width and height of the page
width = page.rect.width
height = page.rect.height
print(f"Width: {width} points")
print(f"Height: {height} points")
'''

# pdf to image->image to data->data in .txt file
'''
#read content from pdf and create images

from pdf2image import convert_from_path
pages = convert_from_path('first.pdf', poppler_path="C:\\Users\\Yashwanth.Akuthota\\Desktop\\jquery\\poppler-24.07.0\\Library\\bin")

for count, page in enumerate(pages):
    page.save(f'out{count}.jpg', 'JPEG')
'''
'''
from PIL import Image 
from pytesseract import pytesseract 
path_to_tesseract = r"C:\\Users\\Yashwanth.Akuthota\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
image_path = "C:\\Users\\Yashwanth.Akuthota\\Desktop\\jquery\\images"
pytesseract.tesseract_cmd = path_to_tesseract 
 

for i in range(14):
    image_path = f"C:\\Users\\Yashwanth.Akuthota\\Desktop\\jquery\\images\\out{i}.jpg"
    #image_path = f"testing{i}.png"
    text = pytesseract.image_to_string(image_path) 
    file = open("pdf_text.txt","a")
    file.write(text[:-1])
    #print(text[:-1])
'''
# Import the required modules
from pdf2docx import Converter

# Keeping the PDF's location in a separate variable
pdf_file = "C:\\Users\\Yashwanth.Akuthota\\Desktop\\jquery\\first.pdf";

# Maintaining the Document's path in a separate variable
docx_file ="C:\\Users\\Yashwanth.Akuthota\\Desktop\\jquery\\first.docx";

# Using the built-in function, convert the PDF file to a document file by saving it in a variable.
cv = Converter(pdf_file)

# Storing the Document in the variable's initialised path
cv.convert(docx_file)

# Conversion closure through the function close()
cv.close()