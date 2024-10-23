import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import UIElements as uel
import os
import sys
import threading
import multiprocessing


class Root:  # ihsliufhnbpo J< PBNÜE<!

    def __init__(self) -> None:

        self.initialize_main_window()

        self.setup_windows()

        self.setup_event_bindings()

        self.root.mainloop()

        pass

    # ------------------------------------------------------------------------
    # setup functions

    def initialize_main_window(self):

        self.root = tk.Tk(screenName=">.<")
        self.root.update_idletasks()

        self.root.title("Main Window")

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.min_width = 800
        self.min_height = 800
        self.general_padx = 4
        self.general_pady = 4

        window_x_offset = self.root.winfo_rootx()
        window_y_offset = self.root.winfo_rooty()

        self.usable_width = self.screen_width - window_x_offset
        self.usable_height = self.screen_height - window_y_offset

    def setup_windows(self):

        self.root.configure(height=self.usable_height, width=self.usable_width)
        self.root.update_idletasks()

        # self.MenuBand = uel.MenuBand(reference_script=self, canvas = self.root)
        self.SplitBox1 = uel.SplitContainer(
            reference_script=self,
            canvas=self.root,
            orientation="h",
            fraction=0.5,
            sizemode="fill",
            padding={"t": 4, "b": 0, "l": 0, "r": 0},
        )
        self.SplitBox1.split_fixed = False
        # self.children = {"SplitBox1": self.root}

        return

    def setup_event_bindings(self):

        self.root.bind("<Configure>", self._on_resizing)

    # ========================================================================
    #       # Update Functions

    def update_sizes(self):

        for child in self.children.values():

            child.update_size()
            continue
        pass

    # ------------------------------------------------------------------------
    # event based functions

    def _on_resizing(self, sender):

        self.update_sizes()

    def _on_closing(self, sender):

        self.root.destroy()


if __name__ == "__main__":
    interface1 = Root()
