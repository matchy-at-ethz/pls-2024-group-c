from pathlib import Path
import os
import sys
from PyQt5 import QtWidgets
from qtpy.QtWidgets import QApplication

if __name__ == "__main__":                          #I COULDNT FIGURE OUT WHY FOR THE LOVE OF GOD IT REQUIRES DIFFERENT IMPORT PATHS REGARDING HOW IT IS RUN
    from Commands import CommandStruct
    from ModeWindows.Default import DefaultScene
    from ModeWindows.Expanded import ExpandedScene
    from ModeWindows.Dynamic import DynamicScene
    from Processes import ProcessStruct
    from Loadwindow import LoadWindow
    from Mainwindow_Ui import Ui_MainWindow

if not __name__ == "__main__":
    from .Commands import CommandStruct
    from .ModeWindows.Default import DefaultScene
    from .ModeWindows.Expanded import ExpandedScene
    from .ModeWindows.Dynamic import DynamicScene
    from .Processes import ProcessStruct
    from .Loadwindow import LoadWindow
    from .Mainwindow_Ui import Ui_MainWindow

ROOT_DIR: Path = Path(__file__).parent.parent.parent.resolve()
exec(open(ROOT_DIR / "Projectconfiguration.py", encoding="utf-8").read())


class SceneTree:

    def __init__(self) -> None:

        app = QApplication(sys.argv)
        
        self.setup_attributes()

        self.initialize_main_window()

        #self.setup_windows()

        #self.setup_event_bindings()

        sys.exit(app.exec_())
        pass

    # ------------------------------------------------------------------------
    # setup functions

    def setup_attributes(self):
        self.current_scene = None
        self.processes = ProcessStruct(self)
        self.command = CommandStruct(self)

        self.SideWindow = QtWidgets.QDialog()
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setWindowOpacity(0)
        self.MainWindow.show()
        

        self.screen_geometry = QApplication.primaryScreen().geometry()
        self.screen_width = self.screen_geometry.width()
        self.screen_height = self.screen_geometry.height()

        # Set window dimensions to half of the screen size
        self.window_width = self.screen_width // 2
        self.window_height = self.screen_height // 2


        # Center the window on the screen
        self.x = (self.screen_width - self.window_width) // 2
        self.y = (self.screen_height - self.window_height) // 2


    def loadConfigurations(self):

        pass


    def initialize_main_window(self):


        self.MainWindow.setWindowOpacity(0)
        self.loadWindow = LoadWindow(scene_tree=self, MainWindow=self.SideWindow)
        
        self.screen = Ui_MainWindow()
        self.MainWindow.resize(self.window_width, self.window_height)
        self.MainWindow.move(self.x, self.y)
        #self.MainWindow.showFullScreen()
        self.screen.setupUi(self.MainWindow, ROOT_DIR , commands = self.command)


    def loaddata(self):
        pass

    def setup_windows(self):

        return


    def setup_event_bindings(self):

        pass

    # ========================================================================
    #       # Update Functions

    def update_sizes(self):
        pass


    def exit_fullscreen(self, event=None):
        pass


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



if __name__ == "__main__":
    
    a = SceneTree()

    
