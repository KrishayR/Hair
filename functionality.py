import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Hair")
root.geometry("1200x700")
root.resizable(0, 0)
canvas = tk.Canvas(root, height=700, width=1200, highlightthickness=0)
canvas.pack()
img_file = Image.open("gui_assets/bg_func.png")
bg = ImageTk.PhotoImage(img_file)
bg_label = canvas.create_image((0,0), image=bg, anchor=tk.N+tk.W)

def cam(hair):
    from video import pick
    pick(hair)

fade_b = ImageTk.PhotoImage(Image.open("gui_assets/fade.png"))
mushroom_b = ImageTk.PhotoImage(Image.open("gui_assets/mushroom.png"))
bangs_b = ImageTk.PhotoImage(Image.open("gui_assets/bangs.png"))
anime_b = ImageTk.PhotoImage(Image.open("gui_assets/anime.png"))
afro_b = ImageTk.PhotoImage(Image.open("gui_assets/afro.png"))

fade = canvas.create_image((200,475), image=fade_b)
canvas.tag_bind(fade, "<Button-1>", lambda h: cam("fade"))

mushroom = canvas.create_image((400,475), image=mushroom_b)
canvas.tag_bind(mushroom, "<Button-1>", lambda h: cam("mushroom"))

bangs = canvas.create_image((600,475), image=bangs_b)
canvas.tag_bind(bangs, "<Button-1>", lambda h: cam("bangs"))

anime = canvas.create_image((800,475), image=anime_b)
canvas.tag_bind(anime, "<Button-1>", lambda h: cam("anime"))

afro = canvas.create_image((1000,475), image=afro_b)
canvas.tag_bind(afro, "<Button-1>", lambda h: cam("afro"))

root.mainloop()
