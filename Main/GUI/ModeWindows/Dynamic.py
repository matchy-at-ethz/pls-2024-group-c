import tkinter as tk
from tkinter import filedialog, ttk, font
import Pmw
from pathlib import Path
import os
import sys
import threading

if __name__ == "__main__":
    from BaseScene import BaseScene


if not __name__ == "__main__":
    from .BaseScene import BaseScene


class DynamicScene(BaseScene):

    def __init__(self, master, scene_tree):

        super().__init__(master, scene_tree)

        self.initializeWidgets() 

    def initializeWidgets(self):

        self.ParametersPanel.config(background="orange")
        self.PlotPanel.config(background="blue")

        self.StartButton = tk.Button(master= self.ParametersPanel, text="start", command= self.runAnalysis)
        self.StartButton.place(x=200, y=200)

    @property
    def parameters(self):

        return 
    
    def runAnalysis(self):
        print("2")
        thread = threading.Thread(target= lambda : self.SceneTree.processes.runAnalysis(self.parameters))
        thread.start()    



    # ------------------------------------------------------------------------
    # event based functions
    
    def _on_enabled(self):
        pass

    def _on_disabled(self):
        pass

    def _on_simulation_completed(self):
        pass