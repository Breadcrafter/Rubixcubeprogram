import random
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

f2l_random = ["F2L-1","F2L-2","F2L-3","F2L-4","F2L-5","F2L-6","F2L-7","F2L-8","F2L-9","F2L-10","F2L-11","F2L-12","F2L-13","F2L-14","F2L-15","F2L-16","F2L-17","F2L-18","F2L-19","F2L-20","F2L-21","F2L-22","F2L-23","F2L-24","F2L-25","F2L-26","F2L-27","F2L-28","F2L-29","F2L-30","F2L-31","F2L-32","F2L-33","F2L-34","F2L-35","F2L-36","F2L-37","F2L-38","F2L-39","F2L-40","F2L-41"]

global label_font
label_font = ("Segoe UI", 20)

# Initialize these variables at the beginning so they can be accessed globally
f2l_frame = None
f2l_label = None
f2l_1_scramble = None
f2l_setup = None
f2l_solve = None
f2l_solution = None
first_image_size = (50, 50)  # Initial size

def how_to_use():
    messagebox.showinfo("How to use this program", "Test text replace later")

def f2l_algorithms(image_size=(50, 50)):
    global f2l_frame
    global f2l_label
    global f2l_1_scramble
    global first_image_size
    global f2l_setup
    global f2l_solve
    global f2l_solution

    f2l_button.destroy()
    oll_button.destroy()
    pll_button.destroy()
    how_to_button.destroy()
    quit_button.destroy()

    # Destroy existing widgets if they exist
    if f2l_frame:
        f2l_frame.destroy()
    if f2l_label:
        f2l_label.destroy()
    if f2l_1_scramble:
        f2l_1_scramble.destroy()
    if f2l_setup:
        f2l_setup.destroy()
    if f2l_solve:
        f2l_solve.destroy()
    if f2l_solution:
        f2l_solution.destroy()

    # Create new widgets
    f2l_current = random.choice(f2l_random)
    f2l_frame = Frame(root, width=first_image_size[0], height=first_image_size[1])
    f2l_frame.pack()

    if f2l_current == "F2L-1":
        f2l_image = Image.open("F2L 1.png")
        f2l_1_scramble = tk.Label(root, text="F R' F' R", font=label_font)
        f2l_1_scramble.place(x=150, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-2":
        f2l_image = Image.open("F2L 2.png")
        f2l_1_scramble = tk.Label(root, text="R' F R F'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="F R' F' R", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-3":
        f2l_image = Image.open("F2L 3.png")
        f2l_1_scramble = tk.Label(root, text="F' U F", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="F' U' F", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-4":
        f2l_image = Image.open("F2L 4.png")
        f2l_1_scramble = tk.Label(root, text="R U' R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R U R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-5":
        f2l_image = Image.open("F2L 5.png")
        f2l_1_scramble = tk.Label(root, text="R U R' U2' R U' R' U", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U' R U R' U2 R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-6":
        f2l_image = Image.open("F2L 6.png")
        f2l_1_scramble = tk.Label(root, text="F' U' F U2' F' U F U'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U' r U' R' U R U r'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-7":
        f2l_image = Image.open("F2L 7.png")
        f2l_1_scramble = tk.Label(root, text="R U R' U2' R U2' R' U", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U' R U2 R' U' R U2 R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-8":
        f2l_image = Image.open("F2L 8.png")
        f2l_1_scramble = tk.Label(root, text="r' U' R2 U' R2' U2' r", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="d R' U2 R U R' U2 R", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-9":
        f2l_image = Image.open("F2L 9.png")
        f2l_1_scramble = tk.Label(root, text="F' U F U' R U R' U", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U' R U' R' U F' U' F", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-10":
        f2l_image = Image.open("F2L 10.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U' R U' R' U", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U' R U R' U R U R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-11":
        f2l_image = Image.open("F2L 11.png")
        f2l_1_scramble = tk.Label(root, text="F' U F U' R U2' R' U", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U' R U2 R' U F' U' F", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-12":
        f2l_image = Image.open("F2L 12.png")
        f2l_1_scramble = tk.Label(root, text="R U R' U2' R U R' U' R U R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R' U2 R2 U R2 U R", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-13":
        f2l_image = Image.open("F2L 13.png")
        f2l_1_scramble = tk.Label(root, text="r U2' R' U R U' R' U M", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="y' U R' U R U' R' U' R", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-14":
        f2l_image = Image.open("F2L 14.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U' R U R' U", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U' R U' R' U R U R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-15":
        f2l_image = Image.open("F2L 15.png")
        f2l_1_scramble = tk.Label(root, text="R U R' U' R U R' U2' R U' R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R' D' R U' R' D R U R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-16":
        f2l_image = Image.open("F2L 16.png")
        f2l_1_scramble = tk.Label(root, text="F' U F U2' R U R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R U' R' U2 F' U' F", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-17":
        f2l_image = Image.open("F2L 17.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U R U2' R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R U2 R' U' R U R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-18":
        f2l_image = Image.open("F2L 18.png")
        f2l_1_scramble = tk.Label(root, text="R U R' U' R U R' F R' F' R", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R' F R F' R U' R' U R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-19":
        f2l_image = Image.open("F2L 19.png")
        f2l_1_scramble = tk.Label(root, text="R U R' U' R U2' R' U'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U R U2 R' U R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-20":
        f2l_image = Image.open("F2L 20.png")
        f2l_1_scramble = tk.Label(root, text="R U R' F R' F' R2' U R' U", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="y' U' R' U2 R U' R' U R", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-21":
        f2l_image = Image.open("F2L 21.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U2' R U R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U2 R U R' U R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-22":
        f2l_image = Image.open("F2L 22.png")
        f2l_1_scramble = tk.Label(root, text="F' L' U2' L F", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="r U' r' U2 r U r'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-23":
        f2l_image = Image.open("F2L 23.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U R U' R' U2' R U' R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U R U' R' U' R U' R' U R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-24":
        f2l_image = Image.open("F2L 24.png")
        f2l_1_scramble = tk.Label(root, text="R U R' F R U R' U' F'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="F U R U' R' F' R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-25":
        f2l_image = Image.open("F2L 25.png")
        f2l_1_scramble = tk.Label(root, text="F' R U R' U' R' F R", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R' F' R U R U' R' F", font=label_font)
        f2l_solution.place(x=130,y=380)
        
    elif f2l_current == "F2L-26":
        f2l_image = Image.open("F2L 26.png")
        f2l_1_scramble = tk.Label(root, text="F' U' F U R U R' U'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U R U' R' F R' F' R", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-27":
        f2l_image = Image.open("F2L 27.png")
        f2l_1_scramble = tk.Label(root, text="R U R' U' R U R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R U' R' U R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-28":
        f2l_image = Image.open("F2L 28.png")
        f2l_1_scramble = tk.Label(root, text="R' F R F' U R U' R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R U R' U' F R' F' R", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-29":
        f2l_image = Image.open("F2L 29.png")
        f2l_1_scramble = tk.Label(root, text="F R' F' R F R' F' R", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R' F R F' U R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-30":
        f2l_image = Image.open("F2L 30.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U R U' R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R U R' U' R U R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-31":
        f2l_image = Image.open("F2L 31.png")
        f2l_1_scramble = tk.Label(root, text="R U R' F R' F' R U", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U' R' F R F' R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-32":
        f2l_image = Image.open("F2L 32.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U R U' R' U R U' R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R2 U R2 U R2 U2 R2", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-33":
        f2l_image = Image.open("F2L 33.png")
        f2l_1_scramble = tk.Label(root, text="R U R' U2' R U R' U", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U' R U' R' U2 R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-34":
        f2l_image = Image.open("F2L 34.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U2' R U' R' U'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U R U R' U2 R U R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-35":
        f2l_image = Image.open("F2L 35.png")
        f2l_1_scramble = tk.Label(root, text="F' U F U' R U' R' U", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U' R U R' U F' U' F", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-36":
        f2l_image = Image.open("F2L 36.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U2' F R' F' R U2'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="U F' U' F U' R U R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-37":
        f2l_image = Image.open("F2L 37.png")
        f2l_1_scramble = tk.Label(root, text="R U' R U2' F R2' F' U2' R2'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R2 U2 F R2 F' U2 R' U R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-38":
        f2l_image = Image.open("F2L 38.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U R U2' R' U R U' R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R U' R' U' R U R' U2 R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-39":
        f2l_image = Image.open("F2L 39.png")
        f2l_1_scramble = tk.Label(root, text="R U' R' U' R U R' U2' R U' R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R U' R' U R U2 R' U R U' R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-40":
        f2l_image = Image.open("F2L 40.png")
        f2l_1_scramble = tk.Label(root, text="R U R' F U R U' R' F' R U R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="r U' r' U2 r U r' R U R'", font=label_font)
        f2l_solution.place(x=130,y=380)

    elif f2l_current == "F2L-41":
        f2l_image = Image.open("F2L 41.png")
        f2l_1_scramble = tk.Label(root, text="R F U R U' R' F' U' R'", font=label_font)
        f2l_1_scramble.place(x=130, y=260)
        f2l_setup = tk.Label(root, text="Setup: ", font=label_font)
        f2l_setup.place(x=200,y=200)
        f2l_solve = tk.Label(root, text="Solve:", font=label_font)
        f2l_solve.place(x=200,y=320)
        f2l_solution = tk.Label(root, text="R U' R' r U' r' U2 r U r'", font=label_font)
        f2l_solution.place(x=130,y=380)




    # Resize image using the size of the first image displayed
    f2l_image = f2l_image.resize(first_image_size, Image.LANCZOS)  # Use Image.ANTIALIAS here
    f2l_image = ImageTk.PhotoImage(f2l_image)
    f2l_label = Label(f2l_frame, image=f2l_image)
    f2l_label.image = f2l_image  # Keep a reference to the image
    f2l_label.place(x=1, y=-1)


def oll_algorithms():
    f2l_button.destroy()
    oll_button.destroy()
    pll_button.destroy()
    how_to_button.destroy()
    quit_button.destroy()

    if f2l_frame:
        f2l_frame.destroy()
    if f2l_label:
        f2l_label.destroy()
    if f2l_1_scramble:
        f2l_1_scramble.destroy()
    if f2l_setup:
        f2l_setup.destroy()
    if f2l_solve:
        f2l_solve.destroy()
    if f2l_solution:
        f2l_solution.destroy()

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

    if f2l_frame:
        f2l_frame.destroy()
    if f2l_label:
        f2l_label.destroy()
    if f2l_1_scramble:
        f2l_1_scramble.destroy()
    if f2l_setup:
        f2l_setup.destroy()
    if f2l_solve:
        f2l_solve.destroy()
    if f2l_solution:
        f2l_solution.destroy()
    
    f2l_button = tk.Button(root, text="F2L", height=3, width=18, command=lambda: f2l_algorithms(first_image_size))
    f2l_button.place(x=18, y=220)

    oll_button = tk.Button(root, text="OLL", height=3, width=18, command=oll_algorithms)
    oll_button.place(x=180, y=220)

    pll_button = tk.Button(root, text="PLL", height=3, width=18, command=pll_algorithms)
    pll_button.place(x=345, y=220)

    quit_button = tk.Button(root, text="Quit", height=3, width=18, command=root.quit)
    quit_button.place(x=18, y=350)

    how_to_button = tk.Button(root, text="How to use", height=3, width=18, command=how_to_use)
    how_to_button.place(x=345, y=350)

def on_space_press(event):
    if event.keysym == "a":
        f2l_algorithms()
   # if event.keysym == "Return":
       # start()
    if event.keysym == "s":
        oll_algorithms()
    if event.keysym == "d":
        pll_algorithms()

root = tk.Tk()
root.geometry("500x500")
root.configure(bg="white")
root.bind('<Escape>', lambda e: root.quit())  # Bind escape key to quit the application
root.bind('<a>', on_space_press)  # Bind enter key to trigger f2l_algorithms
#root.bind("<Return>",on_space_press)
root.bind("<s>", on_space_press)
root.bind("<d>", on_space_press)

# Load the first image and get its size
first_image = Image.open("F2L 1.png")
first_image_size = first_image.size

start()
root.mainloop()
