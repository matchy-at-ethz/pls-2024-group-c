
from pathlib import Path
import os
import sys
import threading

if __name__ == "__main__":
    from BaseScene import BaseScene


if not __name__ == "__main__":
    from .BaseScene import BaseScene


class DefaultScene(BaseScene):

    def __init__(self, master, scene_tree):

        super().__init__(master, scene_tree)

        self.initializeWidgets() 

    def initializeWidgets(self):

        pass

    @property
    def parameters(self):

        return
    
    def runAnalysis(self):
        
        thread = threading.Thread(target= lambda : self.SceneTree.processes.runAnalysis(self.parameters))
        thread.start()        


    # ------------------------------------------------------------------------
    # event based functions
    
    def _on_enabled(self):
        pass

    def _on_disabled(self):
        pass

    def _on_closing(self):
        pass






    