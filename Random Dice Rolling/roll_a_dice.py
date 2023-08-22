"""
author: sumeyye acar
date: 8-21-2023
file: roll_a_dice.py
"""

# if the libraries aren't present in you system type in terminal (without the quotation marks and brackets): 
# "pip install [library-name]"

# importing needed libraries
import tkinter as tk
import random
from PIL import Image, ImageTk


# initiate the main window to hold the application
main = tk.Tk()
main.geometry( "400x300" )
main.title( "Roll A Dice" )


# add labels
label1 = tk.Label( main, text="Are you feelling lucky today?", fg='blue',
                    font= "Helvetice 15 bold" )
label1.pack()


# die icons(make sure to give the actual full path of your icons)
dice = ['die1.png']
dice.append('die2.png')
dice.append('die3.png')
dice.append('die4.png')
dice.append('die5.png')
dice.append('die6.png')

# randomly choosing one of the icons
luck = ImageTk.PhotoImage( Image.open( random.choice( dice ) ) )


# label of the image
label2 = tk.Label( main, image= luck )
label2.image = luck
label2.pack( expand=True ) # packing in the parent widget 


# funtion activating the roll
def roll_a_dice():
    new_iamge = ImageTk.PhotoImage( Image.open( random.choice(dice) ) )
    # update image and keep references
    label2.configure( image=  new_iamge)
    label2.image = new_iamge


# creating and adding a 'roll' button
roll_b = tk.Button( main, text= "Click to Roll!", font="Helvetica 20 bold", fg="blue",bg= 'pink',
                    command=roll_a_dice,  height= 1, width= 10 )
roll_a_dice


# pack in the parent widget
roll_b.pack( expand= True )


# call the mainloop of ImageTK which keeps the window open
main.mainloop()
