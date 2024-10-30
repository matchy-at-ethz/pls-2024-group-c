import tkinter as tk
from tkinter import filedialog, ttk, font
import Pmw
from pathlib import Path
import os
import sys

class BaseScene:

    def __init__(self, master, scene_tree):

        self.master = master 
        self.SceneTree = scene_tree

        self.setupWidgets()

        self.setupConnections()

        pass


    def setupWidgets(self):

        self.root = ttk.Frame(self.master)
        self.root.pack(fill="both", expand=1)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=1)

        # Create frames for each tab
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)

        # Add frames to the notebook
        self.notebook.add(self.tab1, text="Parameters")
        self.notebook.add(self.tab2, text="Plots")

        # Add content to Tab 1
        self.ParametersPanel = tk.Frame(self.tab1)
        self.ParametersPanel.pack(fill="both", expand = 1)

        # Add content to Tab 2
        self.PlotPanel = tk.Frame(self.tab2)
        self.PlotPanel.pack(fill="both", expand = 1)

        #self.button2 = tk.Button(self.tab2, text="Plots", command=lambda: self.SceneTree.command.tab_swich(self.name))



    def setupConnections(self):

        self.SceneTree.root.bind("<Configure>", self._on_configure)


    def disable(self):

        #self.SceneTree.change_visibility_recursively(self.root, False)
        return
    

    def enable(self):

        #self.SceneTree.change_visibility_recursively(self.root, True)
        return
    

    def update(self):
        pass


    def _on_configure(self, sender):
        pass

    def _on_closing(self):
        pass













