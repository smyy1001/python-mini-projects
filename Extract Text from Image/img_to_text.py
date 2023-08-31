"""
author: sumeyye acar
"""

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract

# 'Tesseract-OCR\\tesseract.exe' position
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Main Frame
frame = Tk()
frame.title( 'Extracting Text from Image' )

# Text Widget
upld_img = Label( frame )
text_box = Text( frame, wrap=WORD, height= 10, width= 50, font=( 'Times', 15 ) )
text_box.pack( fill= BOTH, expand= YES )

# Extract Function
def extract_text( path ):
    # First clear old text
    text_box.delete( '1.0', END ) 

    # get the image
    chosen_img = cv2.imread( path )
    temp_img = cv2.resize( chosen_img, ( 400, 350 ) )
    temp_img =cv2.cvtColor( temp_img, cv2.COLOR_BGR2RGB )
    all_texts = pytesseract.image_to_data( temp_img )
    
    temp_text = ""
    prevy = 0

    for count, words in enumerate( all_texts.splitlines() ):
        if count == 0:
            continue
        words = words.split()
        if len( words ) == 12:
            x, y = int(words[6]), int(words[7])
            if prevy - y >= 10 or y - prevy >= 10:
                text_box.insert( END, temp_text + '\n' )
                temp_text = ""
            temp_text = temp_text + words[11] + " "
            prevy = y
    text_box.insert( END, temp_text + '\n' )


# Image Uploader Function
def upload_image():
    try:
        img_path = filedialog.askopenfilename()
        image = Image.open(img_path)
        img = ImageTk.PhotoImage( image )
        upld_img.configure( image= img )
        upld_img.image = img
        extractButton.config( command= lambda: extract_text( img_path ) )
        extractButton.pack()
    except Exception as E:
        print( E )


uploadButton = Button( frame, text= "Choose image", bg= 'pink', fg= 'white', command= upload_image, height= 2, width= 20, font= ('Times', 15, 'bold') )
uploadButton.pack()

upld_img.pack( pady= 10 )
extractButton = Button( frame, text= "Extract the Text", bg= 'pink', fg= 'white', pady=15, padx= 15, font=( 'Time', 15, 'bold' ) )
# extractButton is not packed initially


# keep the frame open
frame.mainloop()
