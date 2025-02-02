from PyQt5 import QtCore, QtGui, QtWidgets
from qtpy.QtGui import QIcon

from gillespie import __package__ as NAME
from gillespie import __version__ as VERSION
from gillespie import get_package_root

from .config import COLOUR, DOCUMENTATION, GIT, RELEASES


class Ui_MainWindow(object):
    def __init__(self):
        self.presets = {}
        self.active_preset = ""

    def setupUi(self, MainWindow, ROOT_DIR, commands):
        self.commands = commands
        MainWindow.setObjectName(f"{NAME} v{VERSION}")
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(QIcon(str(get_package_root() / "assets" / "Logo.ico")))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(521, 555, 521, 555))
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_12.setDirection(QtWidgets.QBoxLayout.BottomToTop)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_12.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1435, 23))
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
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
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
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionDynamic = QtWidgets.QAction(MainWindow)
        self.actionDynamic.setObjectName("actionDynamic")
        self.actionExpanded = QtWidgets.QAction(MainWindow)
        self.actionExpanded.setObjectName("actionExpanded")
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
        self.menuMode.addAction(self.actionDefault)
        self.menuMode.addAction(self.actionExpanded)
        self.menuMode.addSeparator()
        self.menuMode.addAction(self.actionDynamic)
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionDocumentation)
        self.toolBar.addAction(self.actionGit)
        self.toolBar_2.addAction(self.actionDefault)
        self.toolBar_2.addAction(self.actionDynamic)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionExpanded)
        self.toolBar_3.addAction(self.actionCreate_Plot)
        self.connect_menu_actions()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menuData.setTitle(f"{NAME} v{VERSION}")

        self.pushButton_2.setText(_translate("MainWindow", "Add Default Preset"))
        self.pushButton.setText(_translate("MainWindow", "Add Expanded Preset"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.menuExport_Config_to.setTitle(
            _translate("MainWindow", "Export Config to..")
        )
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.menuExport_History_to.setTitle(
            _translate("MainWindow", "Export History to ")
        )
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionCsv.setText(_translate("MainWindow", "Csv"))
        self.actionH5.setText(_translate("MainWindow", "H5"))
        self.actionJson.setText(_translate("MainWindow", "Json"))
        self.actionYaml.setText(_translate("MainWindow", "Yaml"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionKey_Binding.setText(_translate("MainWindow", "Shortkeys"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionDocumentation.setShortcut(_translate("MainWindow", "Ctrl+Alt+H"))
        self.actionGit.setText(_translate("MainWindow", "Git"))
        self.actionGit.setShortcut(_translate("MainWindow", "Ctrl+Alt+G"))
        self.actionReleases.setText(_translate("MainWindow", "Releases"))
        self.actionLicence.setText(_translate("MainWindow", "Licence"))
        self.actionFullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.actionFullscreen.setShortcut(_translate("MainWindow", "Ctrl+Alt+Q"))
        self.actionColors.setText(_translate("MainWindow", "Colors"))
        self.actionJson_2.setText(_translate("MainWindow", "Json"))
        self.actionCsv_2.setText(_translate("MainWindow", "Csv"))
        self.actiontxt.setText(_translate("MainWindow", "Text"))
        self.actionCreate_Plot.setText(_translate("MainWindow", "Create Plot"))
        self.actionDefault.setText(_translate("MainWindow", "Default"))
        self.actionDefault.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionDynamic.setText(_translate("MainWindow", "Dynamic"))
        self.actionDynamic.setShortcut(_translate("MainWindow", "Ctrl+Alt+D"))
        self.actionExpanded.setText(_translate("MainWindow", "Expanded"))
        self.actionExpanded.setShortcut(_translate("MainWindow", "Ctrl+E"))

    def connect_menu_actions(self):

        self.actionExpanded.triggered.connect(
            lambda: self.commands.switchScene("Expanded")
        )
        self.actionDefault.triggered.connect(
            lambda: self.commands.switchScene("Default")
        )

        self.actionExit.triggered.connect(lambda: self.commands.exit())

        self.actionGit.triggered.connect(lambda: self.commands.open_url(GIT))
        self.actionDocumentation.triggered.connect(
            lambda: self.commands.open_url(DOCUMENTATION)
        )
        self.actionReleases.triggered.connect(lambda: self.commands.open_url(RELEASES))
        self.pushButton.clicked.connect(lambda: self.commands.add_preset("Expanded"))
        self.pushButton_2.clicked.connect(lambda: self.commands.add_preset("Default"))
        pass

    def add_preset(self, name: str, path: str):
        """Adds a path to parameter savefiles"""
        if self.active_preset == "":
            self.active_preset = name

        frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)

        if "Default" in path:
            color1 = "#FFFFFF"

        else:
            color1 = "#FFFF00"

        frame.setStyleSheet(f"background-color: {color1};")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        frame.setSizePolicy(sizePolicy)
        hbox = QtWidgets.QHBoxLayout(frame)
        spacer = QtWidgets.QSpacerItem(
            0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        label = QtWidgets.QPushButton(frame)
        pushbutton = QtWidgets.QPushButton(frame)

        label.setText(name)
        label.setSizePolicy(sizePolicy)
        label.setFixedHeight(20)
        pushbutton.setText("X")
        pushbutton.setFixedSize(20, 20)
        pushbutton.setSizePolicy(sizePolicy)
        pushbutton.clicked.connect(lambda: self.commands.remove_preset(name))
        label.clicked.connect(lambda: self.commands.set_preset_active(name))

        hbox.addWidget(label)
        hbox.addItem(spacer)
        hbox.addWidget(pushbutton)

        self.verticalLayout_12.addWidget(frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        entry = {"path": path, "frame": frame}
        self.presets[name] = entry
        self.verticalLayout_12.update()
        self.scrollArea.update()

        self.update_values(self.commands.load_parameters(path))
        self.change_activated_preset(name)

    def remove_preset(self, name: str):
        """Removes the selected path to data files"""
        self.presets[name]["frame"].close()

        self.presets.pop(name)
        if name == self.active_preset:

            self.change_activated_preset(next(iter(self.presets.keys())))

    def change_activated_preset(self, name: str):
        """Changes the selected path to data files"""
        if name == self.active_preset:
            return

        if "Default" in self.presets[name]["path"]:
            color2 = "#F00000"

        if not "Default" in self.presets[name]["path"]:
            color2 = COLOUR

        try:
            if "Default" in self.presets[self.active_preset]["path"]:
                color1 = "#FFFFFF"

            if not "Default" in self.presets[self.active_preset]["path"]:
                color1 = "#FFFF00"

            self.presets[self.active_preset]["frame"].setStyleSheet(
                f"background-color: {color1};"
            )
        except:
            pass
        self.active_preset = name
        self.presets[self.active_preset]["frame"].setStyleSheet(
            f"background-color: {color2};"
        )
        pass

    def update_values(self, new_values):
        pass
