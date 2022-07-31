import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Hair")
root.geometry("1200x700")
root.resizable(0, 0)
img_file = Image.open("gui_assets/background_gui.png")
start_btn_img = Image.open("gui_assets/start_button.png")
bg = ImageTk.PhotoImage(img_file)
start_btn = ImageTk.PhotoImage(start_btn_img)

def nextPage(event):
   root.destroy()
   import functionality

canvas = tk.Canvas(root, height=700, width=1200, highlightthickness=0)
canvas.pack()

bg_label = canvas.create_image((0,0), image=bg, anchor=tk.N+tk.W)

start_button = canvas.create_image((600,475), image=start_btn)
canvas.tag_bind(start_button, "<Button-1>", nextPage)


root.mainloop()
