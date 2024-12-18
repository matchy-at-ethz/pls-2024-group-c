import sys
from pathlib import Path

from PyQt5 import QtWidgets
from qtpy.QtWidgets import QApplication

from gillespie import get_package_root

from .Commands import CommandStruct
from .Loadwindow import LoadWindow
from .Mainwindow_Ui import Ui_MainWindow
from .ModeWindows.Default import DefaultScene
from .ModeWindows.Dynamic import DynamicScene
from .ModeWindows.Expanded import ExpandedScene

# NOTE: commented out because it is not implemented yet
# from ..core.Processes import ProcessStruct


class SceneTree:
    """Main Script that controls the interface

    Args:
        verbosity: Level of logging verbosity.
    """

    def __init__(self) -> None:

        app = QApplication(sys.argv)

        self.setup_attributes()

        self.initialize_main_window()

        self.setup_windows()

        # self.setup_event_bindings()

        sys.exit(app.exec_())
        pass

    # ------------------------------------------------------------------------
    # setup functions

    def setup_attributes(self):
        """Initializes the Attributes of the class"""
        self.command = CommandStruct(self)
        # self.processes = ProcessStruct()

        self.current_scene = None
        self.scenes = {
            "Default": DefaultScene(self, self.command),
            "Expanded": ExpandedScene(self, self.command),
        }

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
        """Load the configurations file for saved parameters or other options

        return:
            tbd
        """

        pass

    def initialize_main_window(self):
        """Show the Main window to which the other scenes are added to. also show the load window initially

        Args:
            verbosity: Level of logging verbosity.
        """
        self.MainWindow.setWindowOpacity(0)
        self.loadWindow = LoadWindow(scene_tree=self, MainWindow=self.SideWindow)

        self.screen = Ui_MainWindow()
        self.MainWindow.resize(self.window_width, self.window_height)
        self.MainWindow.move(self.x, self.y)
        # self.MainWindow.showFullScreen()
        self.screen.setupUi(self.MainWindow, get_package_root(), commands=self.command)
        self.branch = self.screen.frame

        self.gridLayout = QtWidgets.QHBoxLayout(self.branch)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        for value in self.scenes.values():
            value.setupUi(self.branch)
            value.frame.hide()

        self.swich_scene("Default")

    def loaddata(self):
        pass

    def setup_windows(self):
        """Show the Default mode window initially

        Args:
            verbosity: Level of logging verbosity.
        """
        return

    def swich_scene(self, name):

        if name == self.current_scene:
            return

        if self.current_scene is None:
            self.scenes[name].frame.show()
            self.current_scene = name
            return

        self.scenes[self.current_scene].frame.hide()
        self.scenes[name].frame.show()
        self.current_scene = name

    def setup_event_bindings(self):

        pass

    # ========================================================================
    #       # Update Functions

    def update_sizes(self):
        pass

    def exit_fullscreen(self, event=None):
        pass

    def update_preset_list(self):

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
