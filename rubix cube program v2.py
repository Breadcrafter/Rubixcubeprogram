import random
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

f2l_random = ["F2L-1","F2L-2","F2L-3","F2L-4","F2L-5","F2L-6","F2L-7","F2L-8","F2L-9","F2L-10","F2L-11","F2L-12","F2L-13","F2L-14","F2L-15","F2L-16","F2L-17","F2L-18","F2L-19","F2L-20","F2L-21","F2L-22","F2L-23","F2L-24","F2L-25"]

global label_font
label_font = ("Segoe UI", 20)


def how_to_use():
    messagebox.showinfo("How to use this program", "Test text replace later")

def f2l_algorithms(image_size=(10, 10)):
    f2l_button.destroy()
    oll_button.destroy()
    pll_button.destroy()
    how_to_button.destroy()
    quit_button.destroy()

    f2l_current = random.choice(f2l_random)
    f2l_frame = Frame(root, width=image_size[0], height=image_size[1])
    f2l_frame.pack()


    if f2l_current == "F2L-1":
        f2l_image = Image.open("F2L 1.png")
        f2l_image = f2l_image.resize(image_size, Image.LANCZOS )  # Use Image.ANTIALIAS here
        
        f2l_image = ImageTk.PhotoImage(f2l_image)
        f2l_label = Label(f2l_frame, image=f2l_image)
        f2l_label.image = f2l_image  # Keep a reference to the image
        f2l_label.place(x=1,y=-1)
        f2l_1_scramble = tk.Label(root, text="this is the scramble", font=label_font)
        f2l_1_scramble.place(x=130, y=320)
    elif f2l_current == "F2L-2":
        f2l_image = Image.open("F2L 2.png")
        f2l_image = f2l_image.resize(image_size, Image.LANCZOS )  # Use Image.ANTIALIAS here
        
        f2l_image = ImageTk.PhotoImage(f2l_image)
        f2l_label = Label(f2l_frame, image=f2l_image)
        f2l_label.image = f2l_image  # Keep a reference to the image
        f2l_label.place(x=1,y=-1)
        f2l_1_scramble = tk.Label(root, text="this is the scramble 2", font=label_font)
        f2l_1_scramble.place(x=130, y=320)


def oll_algorithms():
    f2l_button.destroy()
    oll_button.destroy()
    pll_button.destroy()
    how_to_button.destroy()
    quit_button.destroy()

def pll_algorithms():
    f2l_button.destroy()
    oll_button.destroy()
    pll_button.destroy()
    how_to_button.destroy()
    quit_button.destroy()

def start():
    global f2l_button
    global oll_button
    global pll_button
    global how_to_button
    global quit_button

    f2l_button = tk.Button(root, text="F2L", height=3, width=18, command=lambda: f2l_algorithms((200, 200)))

    f2l_button.place(x=18, y=220)

    oll_button = tk.Button(root, text="OLL", height=3, width=18, command=oll_algorithms)
    oll_button.place(x=180, y=220)

    pll_button = tk.Button(root, text="PLL", height=3, width=18, command=pll_algorithms)
    pll_button.place(x=345, y=220)

    quit_button = tk.Button(root, text="Quit", height=3, width=18, command=root.quit)
    quit_button.place(x=18, y=350)

    how_to_button = tk.Button(root, text="How to use", height=3, width=18, command=how_to_use)
    how_to_button.place(x=345, y=350)

root = tk.Tk()
root.geometry("500x500")
root.bind('<Escape>', lambda e: root.quit())  # Bind escape key to quit the application

start()
root.mainloop()
