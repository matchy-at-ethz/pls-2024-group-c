import tkinter as tk
from tkinter import filedialog, ttk, font
from pathlib import Path
import os
import sys

if __name__ == "__main__":                          #I COULDNT FIGURE OUT WHY FOR THE LOVE OF GOD IT REQUIRES DIFFERENT IMPORT PATHS REGARDING HOW IT IS RUN
    from Commands import CommandStruct
    from ModeWindows.Default import DefaultScene
    from ModeWindows.Expanded import ExpandedScene
    from ModeWindows.Dynamic import DynamicScene
    from Processes import ProcessStruct
    from Loadwindow import LoadWindow

if not __name__ == "__main__":
    from .Commands import CommandStruct
    from .ModeWindows.Default import DefaultScene
    from .ModeWindows.Expanded import ExpandedScene
    from .ModeWindows.Dynamic import DynamicScene
    from .Processes import ProcessStruct
    from .Loadwindow import LoadWindow

ROOT_DIR: Path = Path(__file__).parent.parent.parent.resolve()
exec(open(ROOT_DIR / "Projectconfiguration.py", encoding="utf-8").read())

from PyQt5 import QtCore, QtGui, QtWidgets
from qtpy.QtWidgets import QApplication, QMainWindow
from qtpy.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, ROOT_DIR, commands):
        self.commands = commands
        MainWindow.setObjectName(f"{NAME} v{VERSION}")
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(QIcon(os.path.join(ROOT_DIR, r"Resources\Logo.ico")))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1203, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        self.menuExport_Config_to = QtWidgets.QMenu(self.menuData)
        self.menuExport_Config_to.setObjectName("menuExport_Config_to")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAnalyze = QtWidgets.QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        self.menuExport_History_to = QtWidgets.QMenu(self.menuAnalyze)
        self.menuExport_History_to.setObjectName("menuExport_History_to")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionCsv = QtWidgets.QAction(MainWindow)
        self.actionCsv.setObjectName("actionCsv")
        self.actionH5 = QtWidgets.QAction(MainWindow)
        self.actionH5.setObjectName("actionH5")
        self.actionJson = QtWidgets.QAction(MainWindow)
        self.actionJson.setObjectName("actionJson")
        self.actionYaml = QtWidgets.QAction(MainWindow)
        self.actionYaml.setObjectName("actionYaml")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionKey_Binding = QtWidgets.QAction(MainWindow)
        self.actionKey_Binding.setObjectName("actionKey_Binding")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionGit = QtWidgets.QAction(MainWindow)
        self.actionGit.setObjectName("actionGit")
        self.actionReleases = QtWidgets.QAction(MainWindow)
        self.actionReleases.setObjectName("actionReleases")
        self.actionLicence = QtWidgets.QAction(MainWindow)
        self.actionLicence.setObjectName("actionLicence")
        self.actionFullscreen = QtWidgets.QAction(MainWindow)
        self.actionFullscreen.setCheckable(True)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionColors = QtWidgets.QAction(MainWindow)
        self.actionColors.setObjectName("actionColors")
        self.actionJson_2 = QtWidgets.QAction(MainWindow)
        self.actionJson_2.setObjectName("actionJson_2")
        self.actionCsv_2 = QtWidgets.QAction(MainWindow)
        self.actionCsv_2.setObjectName("actionCsv_2")
        self.actiontxt = QtWidgets.QAction(MainWindow)
        self.actiontxt.setObjectName("actiontxt")
        self.actionCreate_Plot = QtWidgets.QAction(MainWindow)
        self.actionCreate_Plot.setObjectName("actionCreate_Plot")
        self.menuExport_Config_to.addSeparator()
        self.menuExport_Config_to.addAction(self.actionCsv)
        self.menuExport_Config_to.addAction(self.actionH5)
        self.menuExport_Config_to.addAction(self.actionJson)
        self.menuExport_Config_to.addAction(self.actionYaml)
        self.menuData.addAction(self.actionLoad)
        self.menuData.addAction(self.actionNew)
        self.menuData.addSeparator()
        self.menuData.addAction(self.menuExport_Config_to.menuAction())
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionExit)
        self.menuView.addAction(self.actionFullscreen)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionColors)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionGit)
        self.menuHelp.addAction(self.actionReleases)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionLicence)
        self.menuExport_History_to.addAction(self.actionJson_2)
        self.menuExport_History_to.addAction(self.actionCsv_2)
        self.menuExport_History_to.addAction(self.actiontxt)
        self.menuAnalyze.addAction(self.menuExport_History_to.menuAction())
        self.menuOptions.addAction(self.actionKey_Binding)
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.create_menu_actions()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.menuExport_Config_to.setTitle(_translate("MainWindow", "Export Config to.."))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.menuExport_History_to.setTitle(_translate("MainWindow", "Export History to "))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionCsv.setText(_translate("MainWindow", "Csv"))
        self.actionH5.setText(_translate("MainWindow", "H5"))
        self.actionJson.setText(_translate("MainWindow", "Json"))
        self.actionYaml.setText(_translate("MainWindow", "Yaml"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionKey_Binding.setText(_translate("MainWindow", "Key Binding"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionGit.setText(_translate("MainWindow", "Git"))
        self.actionReleases.setText(_translate("MainWindow", "Releases"))
        self.actionLicence.setText(_translate("MainWindow", "Licence"))
        self.actionFullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.actionColors.setText(_translate("MainWindow", "Colors"))
        self.actionJson_2.setText(_translate("MainWindow", "Json"))
        self.actionCsv_2.setText(_translate("MainWindow", "Csv"))
        self.actiontxt.setText(_translate("MainWindow", "Text"))
        self.actionCreate_Plot.setText(_translate("MainWindow", "Create Plot"))
    
    def create_menu_actions(self):
                    
        self.actionExit.triggered.connect(lambda : self.commands.exit())


        self.actionGit.triggered.connect(lambda : self.commands.open_url(GIT))
        self.actionDocumentation.triggered.connect(lambda : self.commands.open_url(DOCUMENTATION))
        self.actionReleases.triggered.connect(lambda : self.commands.open_url(RELEASES))

        pass


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

        height = int(self.screen_height*0.75)
        width = int(self.screen_width*0.75)

        x_position = (self.screen_width // 2) - (width // 2)
        y_position = (self.screen_height // 2) - (height // 2)

        self.root.configure(height=self.screen_height, width=self.screen_width)
        self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")
        #self.root.attributes('-fullscreen', True)
        self.root.update_idletasks()

        # ==============================================
        # menu bar

       
        menu_font = font.Font(family="Helvetica", size=9)
        menubar = tk.Menu(self.root)

        # ----------------------------------------------
        # Data

        file_menu = tk.Menu(menubar, tearoff=0, font=menu_font)
        file_menu.add_command(label="Open Config", font=menu_font, command=command.openConfig)
        file_menu.add_command(label="Save Config", font=menu_font, command=command.saveConfig)

        file_menu.add_separator()

        export_submenu = tk.Menu(file_menu, tearoff=0, font=menu_font)
        export_submenu.add_command(label="CSV", font=menu_font, command=lambda: command.exportConfig("CSV"))
        export_submenu.add_command(label="YAML", font=menu_font, command=lambda: command.exportConfig("YAML"))
        export_submenu.add_command(label="JSON", font=menu_font, command=lambda: command.exportConfig("JSON"))
        export_submenu.add_command(label="H5", font=menu_font, command=lambda: command.exportConfig("H5"))
        file_menu.add_cascade(label="Export Config to...", font=menu_font, menu=export_submenu)

        file_menu.add_separator()

        file_menu.add_command(label="Exit", font=menu_font, command=self.exit)
        menubar.add_cascade(label="Start", menu=file_menu, font=menu_font)

        # ----------------------------------------------
        # Mode

        mode_menu = tk.Menu(menubar, tearoff=0, font=menu_font)
        mode_menu.add_command(label="Default", font=menu_font, command=lambda: command.change_mode("default"))
        mode_menu.add_command(label="Expanded", font=menu_font, command=lambda: command.change_mode("expanded"))
        mode_menu.add_command(label="Dynamic", font=menu_font, command=lambda: command.change_mode("dynamic"))
        menubar.add_cascade(label="Mode", menu= mode_menu, font=menu_font)

        # ----------------------------------------------
        # help

        help_menu = tk.Menu(menubar, tearoff=0, font=menu_font)
        help_menu.add_command(label="Documentation", font=menu_font, command=lambda: command.open_url(documentation))
        help_menu.add_command(label="Git", command=lambda: command.open_url(git))
        help_menu.add_command(label="Releases", font=menu_font, command=lambda: command.open_url(releases))
        menubar.add_cascade(label="Help", menu=help_menu, font=menu_font)

        # Display the menubar

        self.root.config(menu=menubar)
        menubar.configure(font=menu_font)
        self.root.update_idletasks()

        # ==============================================
        # Scene Frame

        self.scene_frame = tk.Frame(self.root)
        self.scene_frame.pack(fill=tk.BOTH, expand=True)  # Fill the entire window

        scene_classes = {
            "default" : DefaultScene,
            "expanded": ExpandedScene,
            "dynamic" : DynamicScene
        }
        self.modes_port_frame = ttk.Frame(self.scene_frame)
        self.ModesPort = ScenePort(self, self.modes_port_frame, scene_classes)
        self.ModesPort.set_active("default")

        return


    def setup_event_bindings(self):

        self.root.bind("<Configure>", self._on_resizing)

        self.root.bind("<Escape>", self.exit_fullscreen)

    # ========================================================================
    #       # Update Functions

    def update_sizes(self):
        pass


    def exit_fullscreen(self, event=None):
        # Exit fullscreen mode
        self.root.attributes('-fullscreen', False)


    def change_visibility_recursively(self, widget, value : bool ):

        widget.takefocus = value  # Disable focus on the widget itself
        if value:
            for child in widget.winfo_children():  # Iterate over all children
                self.change_visibility_recursively(child, value)
                continue
            return

        for child in self.root.winfo_children():  # Iterate over all children
            self.change_visibility_recursively(child, value)
            continue
        return 

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


class ScenePort:
    """
    Holds references to several widgets and manages which one will be displayed. 
    """

    def __init__(self, scene_tree, master, child = None, default_scene : str = "default"):

        self.master = master
        self.scene_tree = scene_tree
        self.current_scene = None
        self.current_scene_name = None
        self.children = {}
        self.default_scene = default_scene
        self.master.pack(fill="both", expand=1)

        if type(child) == dict:
            self.children = child
        pass

    def add(self, name, widget):
        self.children[name] = widget
        pass

    def remove(self, name : str):
        self.children.remove(name)
        pass

    def set_active(self, name):

        if self.current_scene is None:
            
            self.current_scene = self.children[self.default_scene](self.master, self.scene_tree)
            self.current_scene_name = self.default_scene
            return
        
        if self.current_scene_name == name:
            return

        self.current_scene.root.destroy()       

        try:
            self.current_scene._on_closing()
        except:
            pass
        
        # Dynamically create a new scene instance from the dictionary
        if name in self.children:
            self.current_scene = self.children[name](self.master, self.scene_tree)
            self.current_scene_name = name

        pass

    def configure(self, *args, **kwargs):
        self.root.configure(*args,*kwargs)
        return



if __name__ == "__main__":
    
    a = SceneTree()

    
