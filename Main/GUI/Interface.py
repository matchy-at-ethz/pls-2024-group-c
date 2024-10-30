import tkinter as tk
from tkinter import filedialog, ttk, font
import Pmw
from pathlib import Path
import os
import sys
import threading
import multiprocessing
import time


if __name__ == "__main__":                          #I COULDNT FIGURE OUT WHY FOR THE LOVE OF GOD IT REQUIRES DIFFERENT IMPORT PATHS REGARDING HOW IT IS RUN
    from Commands import CommandStruct
    from ModeWindows.Default import DefaultScene
    from ModeWindows.Expanded import ExpandedScene
    from ModeWindows.Dynamic import DynamicScene
    from Processes import ProcessStruct
    from Loadwindow import LoadWindow

if not __name__ == "__main__":
    from .Commands import CommandStruct
    from .ModeWindows.Default import DefaultScene
    from .ModeWindows.Expanded import ExpandedScene
    from .ModeWindows.Dynamic import DynamicScene
    from .Processes import ProcessStruct
    from .Loadwindow import LoadWindow

ROOT_DIR: Path = Path(__file__).parent.parent.parent.resolve()
exec(open(ROOT_DIR / "Projectconfiguration.py", encoding="utf-8").read())


class SceneTree:

    def __init__(self) -> None:

        self.processes = ProcessStruct(self)
        self.setup_attributes()

        self.initialize_main_window()

        self.setup_windows()

        self.setup_event_bindings()

        self.root.protocol(
            "WM_DELETE_WINDOW", self.root.quit
        )  # Properly handle window close

        self.root.mainloop()

        pass

    # ------------------------------------------------------------------------
    # setup functions

    def setup_attributes(self):
        self.current_scene = None

    def initialize_main_window(self):

        current_file_path = Path(__file__).resolve()
        root_path = current_file_path.parent.parent.parent

        self.root = tk.Tk(screenName="Mainwindow")
        self.root.iconbitmap(os.path.join(root_path, r"Resources\Logo.ico"))
        self.root.title(f"{NAME} v{VERSION}") # the yellow underline is fine

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.root.withdraw()
        LoadWindow(self.root, self)
        self.root.deiconify()

        Pmw.initialise()





    def loaddata(self):
        pass

    def setup_windows(self):

        height = int(self.screen_height*0.75)
        width = int(self.screen_width*0.75)

        x_position = (self.screen_width // 2) - (width // 2)
        y_position = (self.screen_height // 2) - (height // 2)

        self.root.configure(height=self.screen_height, width=self.screen_width)
        self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")
        #self.root.attributes('-fullscreen', True)
        self.root.update_idletasks()

        # ==============================================
        # menu bar

        command = CommandStruct(self)
        menu_font = font.Font(family="Helvetica", size=9)
        menubar = tk.Menu(self.root)

        # ----------------------------------------------
        # Data

        file_menu = tk.Menu(menubar, tearoff=0, font=menu_font)
        file_menu.add_command(label="Open Config", font=menu_font, command=command.openConfig)
        file_menu.add_command(label="Save Config", font=menu_font, command=command.saveConfig)

        file_menu.add_separator()

        export_submenu = tk.Menu(file_menu, tearoff=0, font=menu_font)
        export_submenu.add_command(label="CSV", font=menu_font, command=lambda: command.exportConfig("CSV"))
        export_submenu.add_command(label="YAML", font=menu_font, command=lambda: command.exportConfig("YAML"))
        export_submenu.add_command(label="JSON", font=menu_font, command=lambda: command.exportConfig("JSON"))
        export_submenu.add_command(label="H5", font=menu_font, command=lambda: command.exportConfig("H5"))
        file_menu.add_cascade(label="Export Config to...", font=menu_font, menu=export_submenu)

        file_menu.add_separator()

        file_menu.add_command(label="Exit", font=menu_font, command=self.exit)
        menubar.add_cascade(label="Start", menu=file_menu, font=menu_font)

        # ----------------------------------------------
        # Mode

        mode_menu = tk.Menu(menubar, tearoff=0, font=menu_font)
        mode_menu.add_command(label="Default", font=menu_font, command=lambda: command.change_mode("default"))
        mode_menu.add_command(label="Expanded", font=menu_font, command=lambda: command.change_mode("expanded"))
        mode_menu.add_command(label="Dynamic", font=menu_font, command=lambda: command.change_mode("dynamic"))
        menubar.add_cascade(label="Mode", menu= mode_menu, font=menu_font)

        # ----------------------------------------------
        # help

        help_menu = tk.Menu(menubar, tearoff=0, font=menu_font)
        help_menu.add_command(label="Documentation", font=menu_font, command=lambda: command.open_url(documentation))
        help_menu.add_command(label="Git", command=lambda: command.open_url(git))
        help_menu.add_command(label="Releases", font=menu_font, command=lambda: command.open_url(releases))
        menubar.add_cascade(label="Help", menu=help_menu, font=menu_font)

        # Display the menubar

        self.root.config(menu=menubar)
        menubar.configure(font=menu_font)
        self.root.update_idletasks()

        # ==============================================
        # Scene Frame

        self.scene_frame = tk.Frame(self.root)
        self.scene_frame.pack(fill=tk.BOTH, expand=True)  # Fill the entire window

        scene_classes = {
            "default" : DefaultScene,
            "expanded": ExpandedScene,
            "dynamic" : DynamicScene
        }
        self.modes_port_frame = ttk.Frame(self.scene_frame)
        self.ModesPort = ScenePort(self, self.modes_port_frame, scene_classes)
        self.ModesPort.set_active("default")

        return


    def setup_event_bindings(self):

        self.root.bind("<Configure>", self._on_resizing)

        self.root.bind("<Escape>", self.exit_fullscreen)

    # ========================================================================
    #       # Update Functions

    def update_sizes(self):
        pass


    def exit_fullscreen(self, event=None):
        # Exit fullscreen mode
        self.root.attributes('-fullscreen', False)


    def change_visibility_recursively(self, widget, value : bool ):

        widget.takefocus = value  # Disable focus on the widget itself
        if value:
            for child in widget.winfo_children():  # Iterate over all children
                self.change_visibility_recursively(child, value)
                continue
            return

        for child in self.root.winfo_children():  # Iterate over all children
            self.change_visibility_recursively(child, value)
            continue
        return 

    # ------------------------------------------------------------------------
    # event based functions

    def _on_resizing(self, sender):

        self.update_sizes()


    def _on_closing(self):

        self.root.destroy()

    
    # ========================================================================
    # Commands

    def exit(self):
        self.root.destroy()


class ScenePort:
    """
    Holds references to several widgets and manages which one will be displayed. 
    """

    def __init__(self, scene_tree, master, child = None, default_scene : str = "default"):

        self.master = master
        self.scene_tree = scene_tree
        self.current_scene = None
        self.current_scene_name = None
        self.children = {}
        self.default_scene = default_scene
        self.master.pack(fill="both", expand=1)

        if type(child) == dict:
            self.children = child
        pass

    def add(self, name, widget):
        self.children[name] = widget
        pass

    def remove(self, name : str):
        self.children.remove(name)
        pass

    def set_active(self, name):

        if self.current_scene is None:
            
            self.current_scene = self.children[self.default_scene](self.master, self.scene_tree)
            self.current_scene_name = self.default_scene
            return
        
        if self.current_scene_name == name:
            return

        self.current_scene.root.destroy()       

        try:
            self.current_scene._on_closing()
        except:
            pass
        
        # Dynamically create a new scene instance from the dictionary
        if name in self.children:
            self.current_scene = self.children[name](self.master, self.scene_tree)
            self.current_scene_name = name

        pass

    def configure(self, *args, **kwargs):
        self.root.configure(*args,*kwargs)
        return



if __name__ == "__main__":
    interface1 = SceneTree()
