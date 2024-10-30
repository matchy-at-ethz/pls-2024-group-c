
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

        pass



    def setupConnections(self):

        pass


    def disable(self):

        return
    

    def enable(self):

        return
    

    def update(self):
        pass


    def _on_configure(self, sender):
        pass

    def _on_closing(self):
        pass













