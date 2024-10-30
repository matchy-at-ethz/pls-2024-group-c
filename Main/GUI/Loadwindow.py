from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, ttk, font
from pathlib import Path
import time

ROOT_DIR: Path = Path(__file__).parent.parent.parent.resolve()
exec(open(ROOT_DIR / "Projectconfiguration.py", encoding="utf-8").read())

class LoadWindow:
    """
    THIS IS ATROCHIOUS DO NOT RESIZE AT ANY COST!!!!!
    """

    def __init__(self, master, scene_tree):

        image = Image.open(r"Resources\image.png")
        new_size = (image.width // 5, image.height // 5)

        load_screen = tk.Toplevel()
        load_screen.config(menu=None, height=new_size[1], width=new_size[0], relief="flat")
        load_screen.overrideredirect(True)
        load_screen.update_idletasks()

        scaled_image = image.resize(new_size)

        x_position = (scene_tree.screen_width // 2) - (new_size[0] // 2)
        y_position = (scene_tree.screen_height // 2) - (new_size[1] // 2)

        # Set window size and position
        load_screen.geometry(f"{new_size[0]}x{new_size[1]}+{x_position}+{y_position}")

        photo = ImageTk.PhotoImage(master=load_screen, image = scaled_image)
        load_screen.photo = photo
        image_frame = tk.Label(master= load_screen, image=photo)
        image_frame.pack(fill="both")

        color = "#BE632E"

        banner = tk.Frame(master = load_screen, background=color)
        banner.place(width=new_size[0], height=int(new_size[1]*0.2), x =0, y= int(new_size[1]*0.8 +1))


        title_font = font.Font(name="Times", size=48)
        title  = tk.Label(master=banner, text= f"{NAME}", font=title_font, background=color, foreground="white")
        title.place(x=5,y=4)
        version_font = font.Font(family="Helvetica", size=8)
        version = tk.Label(master=banner, text= f"Version {VERSION}", font= version_font, background=color, foreground="white")
        version.place(x=180,y=int(new_size[1]*0.2 -20))
        load_screen.update_idletasks()
        
        load_messages_font = font.Font(family="Helvetica", size=18)
        self.load_messages  = tk.Label(master=banner, text= "Loading Data", font= load_messages_font, background=color, foreground="white")

        time.sleep(1.5)
        self.load_messages.place(x=int(new_size[0] -180), y=int(new_size[1]*0.2 -35))
        time.sleep(4) # to simulate loading processes
