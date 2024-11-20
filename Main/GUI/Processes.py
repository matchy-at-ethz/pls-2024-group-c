import threading
import multiprocessing



class ProcessStruct:
    """
    Min Says Multithreading or multiprocessing isn't very useful in python so do not focus on this.
    I intended this to manage multiprocessing
    """
    def __init__(self, scene_tree):

        self.SceneTree = scene_tree

    
    def runAnalysis(self, *args, **kwargs):
        pass
