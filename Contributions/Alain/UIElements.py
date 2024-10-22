import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import sys
import threading
import multiprocessing

class SplitContainer():

    #==================================================================================================
    #       initialization

    def __init__(self, reference_script, canvas, orientation, fraction, margin = {"t": 4, "b" : 4, "l": 4, "r": 4}, padding = {"t": 4, "b" : 4, "l": 4, "r": 4} , sizemode = "fill"):

        self.reference_script = reference_script
        self.canvas = canvas

        self.padding = padding
        self.margin = margin
        self.orientation = orientation
        self.fraction = fraction
        self.split_fixed = False
        self.sizemode = sizemode
        self.size = {}

        self.mouse_down = False

        if sizemode == 'xExpand':
            self.panel1_height = (self.canvas.winfo_height()-1.5*(self.padding["l"] + self.padding["b"]))*fraction
            

        self.setup_panels()

        self.setup_bindings()
    

    def setup_panels(self):

        self.root = ttk.Frame(self.canvas)

        self.panel1 = ttk.Frame(self.root)
        self.panel2 = ttk.Frame(self.root)
        self.children = {"panel1" : self.panel1, "panel2" : self.panel2}

        self.update_size()
    

    def setup_bindings(self):

        self.root.bind("<Enter>", self._on_mouse_entered)
        self.root.bind("<Leave>", self._on_mouse_left)
        self.root.bind("<Button-1>", self._on_mouse_clicked)
        self.root.bind("<ButtonRelease-1>", self._on_mouse_released)
        self.root.bind("<Motion>", self._on_mouse_move)

    #==================================================================================================
    #       Updates

    def update_size(self):

        self.size['x'] = self.canvas.winfo_width()
        self.size['y'] = self.canvas.winfo_height()

        if self.sizemode == 'fill':

            self.update_in_fill()

        if self.sizemode == 'xExpand':

            self.update_in_xExpand()

    def update_in_fill(self):
        
        self.root.place_configure(height=self.size['y'],width=self.size['x'],x=0, y =0)

        if self.orientation == 'h':
            panel1_posx, panel1_posy = [self.padding["l"], self.padding["t"]]
            panel1_width = self.size['x'] - (self.padding["l"] + self.padding["r"]) #account for split
            panel1_height = ((self.size['y']*self.fraction) - 1.5*(self.padding["t"] + self.padding["b"]))

            panel2_posx = panel1_posx
            panel2_posy = panel1_posy + panel1_height + (self.padding["t"] + self.padding["b"])/2
            panel2_width = panel1_width
            panel2_height = ((self.size['y']-panel1_height) - (self.padding["t"]*1.5 + self.padding["b"])) 
        
        if self.orientation == 'v':

            panel1_posx, panel1_posy = [self.padding["t"], self.padding["l"]]
            panel1_height = self.size['y'] - (self.padding["t"] + self.padding["b"])
            panel1_width = ((self.size['x']*self.fraction) - 1.5*(self.padding["l"] + self.padding["r"]))

            panel2_posx = panel1_posx + panel1_width + 0.5*(self.padding["l"] + self.padding["r"])
            panel2_posy = panel1_posy
            panel2_height = panel1_height
            panel2_width = (self.size['x'] - panel1_width) - 1.5*(self.padding["l"] + self.padding["b"])
        

        self.panel1.place_configure(height=panel1_height,width=panel1_width,x=panel1_posx, y =panel1_posy)
        self.panel2.place_configure(height=panel2_height,width=panel2_width,x=panel2_posx, y =panel2_posy)
        

        for child in self.children.values():

            for sub_child in child.children.values():

                sub_child.update_size()
                continue
    
    def update_in_xExpand(self):

        self.root.place_configure(height=self.size['y'],width=self.size['x'],x=0, y =0)

        if self.orientation == 'h':
            panel1_posx, panel1_posy = [self.padding["l"], self.padding["t"]]
            panel1_width = self.size['x'] - (self.padding["l"] + self.padding["r"]) #account for split
            panel1_height = self.panel1_height

            panel2_posx = panel1_posx
            panel2_posy = panel1_posy + panel1_height + (self.padding["t"] + self.padding["b"])/2
            panel2_width = panel1_width
            panel2_height = ((self.size['y']-panel1_height) - (self.padding["t"]*1.5 + self.padding["b"])) 
        
        if self.orientation == 'v':

            panel1_posx, panel1_posy = [self.padding["t"], self.padding["l"]]
            panel1_height = self.size['y'] - (self.padding["t"] + self.padding["b"])
            panel1_width = ((self.size['x']) - 1.5*(self.padding["l"] + self.padding["r"]))

            panel2_posx = panel1_posx + panel1_width + 0.5*(self.padding["l"] + self.padding["r"])
            panel2_posy = panel1_posy
            panel2_height = panel1_height
            panel2_width = (self.size['x'] - panel1_width) - 1.5*(self.padding["l"] + self.padding["b"])
        

        self.panel1.place_configure(height=panel1_height,width=panel1_width,x=panel1_posx, y =panel1_posy)
        self.panel2.place_configure(height=panel2_height,width=panel2_width,x=panel2_posx, y =panel2_posy)
        

        for child in self.children.values():

            for sub_child in child.children.values():

                sub_child.update_size()
                continue

        

    def update_split(self, sender):

        if self.mouse_down and (self.orientation == 'h'):

            self.fraction = sender.y / self.size['y']
            self.update_size()
            return
        
        if self.mouse_down and (self.orientation == 'v'):

            self.fraction = sender.x / self.size['x']
            self.update_size()
            return

    #==================================================================================================
    #       Utility

    def position_on_split(self, x, y, margin):

        if self.orientation == 'h':

            lower_bound = ((self.size['y']*self.fraction) - margin*(self.padding["t"] + self.padding["b"]))
            upper_bound = lower_bound + margin*(self.padding["t"] + self.padding["b"])
            
            if lower_bound < y < upper_bound:
                return True
        
        if self.orientation == 'v':

            lower_bound = ((self.size['x']*self.fraction) - margin*(self.padding["l"] + self.padding["r"]))
            upper_bound = lower_bound + margin*(self.padding["l"] + self.padding["r"])     

            if lower_bound < x < upper_bound:
                return True  

        return False

    #==================================================================================================
    #       Events

    def _on_mouse_entered(self, sender):
        return
    
    def _on_mouse_left(self, sender):
        return
    
    def _on_mouse_clicked(self, sender): #decide whether mouse is in the sweetspot

        if self.position_on_split(sender.x, sender.y, 100) and (not self.split_fixed):
            
            self.mouse_down = True
            return


    def _on_mouse_released(self, sender):
        self.mouse_down = False
        return


    def _on_mouse_move(self, sender):

        if self.mouse_down:
            self.update_split(sender)                
            return

        if self.position_on_split(sender.x, sender.y, 1000) and (not self.split_fixed):      
            
            self.root.configure(cursor = "sb_h_double_arrow")
            self.root.update_idletasks()
        
        self.root.configure(cursor = "arrow")
        self.root.update_idletasks()
        return
    


class MenuBand():

    #==================================================================================================
    #       Initialization

    def __init__(self,reference_script, canvas):

        self.reference_script = reference_script
        self.canvas = canvas

        self.setup_windows()
        return
    
    def setup_windows(self):

        self.frame = ttk.Frame(self.canvas)
        self.size = {}
        self.size['x'] = self.canvas.winfo_width()
        self.size['y'] = self.canvas.winfo_height()  
        self.frame.place_configure(height=self.size['y'],width=self.size['x'],x=0, y =0)
        self.frame.update_idletasks()

        self.splitContainer = SplitContainer(reference_script = self,canvas=self.frame, orientation = 'h', fraction = 0.04, sizemode='xExpand', padding = {"t": 0, "b" : 0, "l": 0, "r": 0})
        self.splitContainer.split_fixed = True
        #self.splitContainer.panel1_height = 400
        self.splitContainer.update_size()
        self.branch = self.splitContainer.panel2

        #self.flowBox = FlowBox(self.splitContainer.panel1, direction = 'Left to Right')
        

    #==================================================================================================
    #       Update

    def update_size(self):

        self.size['x'] = self.canvas.winfo_width()
        self.size['y'] = self.canvas.winfo_height()

        self.branch.update_size()

    #==================================================================================================
    #       Utillity

    #==================================================================================================
    #       Events



class FlowBox():

    #==================================================================================================
    #       Initialization

    def __init__(self, reference_script, direction):
        return

    #==================================================================================================
    #       Update


        def add_object(self, object):
            pass

    #==================================================================================================
    #       Utillity

    #==================================================================================================
    #       Events



class CenterContainer():

    #==================================================================================================
    #       Initialization

    def __init__(self,reference_script, child,  margin = {"t": 4, "b" : 4, "l": 4, "r": 4}, padding = {"t": 4, "b" : 4, "l": 4, "r": 4} , sizemode = "fill"):

        self.reference_script = reference_script
        self.margin = margin
        self.padding = padding
        self.sizemode = sizemode

        self.setup_windows()
        return
    


    #==================================================================================================
    #       Update

    def update_size(self):

        if self.sizemode == 'fill':
            self.size['x'] = self.reference_script.winfo_width()
            self.size['y'] = self.reference_script.winfo_height()
        
        self.root.place_configure(height=self.size['y'],width=self.size['x'],x=0, y =0)


    #==================================================================================================
    #       Utillity

    #==================================================================================================
    #       Events



class ScrollBox():

    #==================================================================================================
    #       Initialization

    def __init__(self,reference_script):
        return

    #==================================================================================================
    #       Update

    #==================================================================================================
    #       Utillity

    #==================================================================================================
    #       Events

