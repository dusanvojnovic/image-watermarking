from tkinter import *
import os
import tkinter.font as font
from PIL import ImageTk, Image, ImageDraw, ImageFont, ImageGrab
from tkinter import filedialog


def submit():
    global canvas
    text = text_var.get()
    canvas.create_text(25, 20, anchor='nw', fill='gray', font=15, text = text)
    text_var.set("")

def open_img():
    global canvas
    img = Image.open(filedialog.askopenfilename(initialdir = "/",title = "Select A File",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))))
    img = img.resize((1250, 700), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    text = text_var.get()
    canvas.image = photo
    canvas.create_image(0,0, image=photo, anchor='nw')
    canvas.place(x=15, y=150)

def save_img():
    global canvas
    x=window.winfo_rootx()+canvas.winfo_x()
    y=window.winfo_rooty()+canvas.winfo_y()
    x1=x+canvas.winfo_width()
    y1=y+canvas.winfo_height()
    box=(x,y,x1,y1)
    grabcanvas = ImageGrab.grab().crop(box)
    grabcanvas.save(fp=filedialog.asksaveasfilename(initialdir = "/",title = "Save Image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")),  defaultextension ='*.jpg'))

window = Tk()
window.title("WatermarkImg")
window.minsize(width = 1400, height = 900)
window.resizable(width = False, height = False)
window.config(padx=70, pady=15, bg="#a1cae2")

text_var = StringVar()

canvas = Canvas(width = 1250, height = 700)
watermark_label = Label(text = "Add watermark text here: ")
watermark_label.config(font = 30)
watermark_label.place(x=220, y=40)
watermark_label.config(bg="#a1cae2")
watermark_entry = Entry(width = 60, textvariable = text_var)
watermark_entry.place(x=460, y =35, width= 270, height = 30)

submit = Button(text = "Submit", command = submit, width=20, height=1)
submit.place(x=880, y = 37)
add_file = Button(text="Select Image", command = open_img, width=15, height=1)
add_file.place(x=300, y=100)
save_file = Button(text = "Save Image", command = save_img, width=15, height=1)
save_file.place(x=750, y=100)


window.mainloop()