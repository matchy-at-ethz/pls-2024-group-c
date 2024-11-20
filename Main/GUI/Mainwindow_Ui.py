from PyQt5 import QtCore, QtGui, QtWidgets
from qtpy.QtWidgets import QApplication, QMainWindow
from qtpy.QtGui import QIcon
from pathlib import Path
import os

from Projectconfiguration import NAME,VERSION, GIT, DOCUMENTATION, RELEASES

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
