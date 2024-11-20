from pathlib import Path
import os
import sys
import threading



class ExpandedScene():

    def __init__(self, master, scene_tree):

        super().__init__(master, scene_tree)

        self.initializeWidgets() 


    def connect_actions(self):
        """Connects Actions to the corresponding Commands"""
        self.pushButton.clicked.connect(lambda : self.commands.start_default(
            self.parameters
            ))
        

        # self.pushButton_2.clicked.connect(self.commands.save_figure)
        # self.pushButton_3.clicked.connect(self.commands.close_figure)
        # self.pushButton_4.clicked.connect(self.commands.add_figure)

        pass


    def add_figure_to_display(self):
        pass




    @property
    def parameters(self):
        """returns the parameters required to run the analysis"""
        parameters = {}

        return parameters