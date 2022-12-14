# How to Extract Images from PDF in Python
from pathlib import Path
import fitz # PyMuPDF
import io
from PIL import Image
import os
import cv2
import base64

# file path you want to extract images from
# file = "byju.pdf"
# open the file
for pdfFile in Path("pdfs").glob("*.pdf"):
    pdf_file = fitz.open(pdfFile)
# iterate over PDF pages
    for page_index in range(len(pdf_file)):
    # get the page itself
       page = pdf_file[page_index]
       image_list = page.get_images()
    # printing number of images found in this page
       if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
       else:
        print("[!] No images found on page", page_index)
       for image_index, img in enumerate(page.get_images(), start=1):
        # get the XREF of the image
        xref = img[0]
        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        # get the image extension
        image_ext = base_image["ext"]
        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))
        
        # save it to local disk
        img = image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))
    
        

                                                                                                                                                                                                                                                                                    
        #Images stored in the folder
        # with open("images/{}.jpg".format(pdfFile.stem), mode='wb') as fiile:
        #     fiile.write(image)
        #     fiile.close        
       
    
    
