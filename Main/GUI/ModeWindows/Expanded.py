from PyQt5 import QtCore, QtGui, QtWidgets

from Main.GUI.ModeWindows.ExpandedModeEntry import EntryBox 


class ExpandedScene():

    def __init__(self, parent, commands):
        self.parent = parent
        self.commands = commands

        self.entry_boxes = []
        pass

    def setupUi(self, branch):
        self.gridLayout = self.parent.gridLayout
        self.frame = QtWidgets.QFrame(branch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(545, 700))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 521, 555))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.addProteinPushButton = QtWidgets.QPushButton(self.frame_5)
        self.addProteinPushButton.setObjectName("addProteinPushButton")
        self.horizontalLayout_3.addWidget(self.addProteinPushButton)
        self.addTFPushButton = QtWidgets.QPushButton(self.frame_5)
        self.addTFPushButton.setObjectName("addTFPushButton")
        self.horizontalLayout_3.addWidget(self.addTFPushButton)
        self.addmRNAPushButton = QtWidgets.QPushButton(self.frame_5)
        self.addmRNAPushButton.setObjectName("addmRNAPushButton")
        self.horizontalLayout_3.addWidget(self.addmRNAPushButton)
        self.toolButton = QtWidgets.QToolButton(self.frame_5)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_3.addWidget(self.toolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_52 = QtWidgets.QFrame(self.frame_3)
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_52)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(4)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_54 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_54)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem11 = QtWidgets.QSpacerItem(424, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem11)
        self.label_26 = QtWidgets.QLabel(self.frame_54)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_17.addWidget(self.label_26)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem12)
        self.trajectoriesSpinBox = QtWidgets.QSpinBox(self.frame_54)
        self.trajectoriesSpinBox.setObjectName("trajectoriesSpinBox")
        self.horizontalLayout_17.addWidget(self.trajectoriesSpinBox)
        self.verticalLayout_14.addWidget(self.frame_54)
        self.frame_53 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_53)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem13 = QtWidgets.QSpacerItem(419, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem13)
        self.label_25 = QtWidgets.QLabel(self.frame_53)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_16.addWidget(self.label_25)
        spacerItem14 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem14)
        self.stepsSpinBox = QtWidgets.QSpinBox(self.frame_53)
        self.stepsSpinBox.setObjectName("stepsSpinBox")
        self.horizontalLayout_16.addWidget(self.stepsSpinBox)
        self.verticalLayout_14.addWidget(self.frame_53)
        self.verticalLayout_40.addWidget(self.groupBox_5)
        self.verticalLayout_3.addWidget(self.frame_52)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem15 = QtWidgets.QSpacerItem(427, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.startPushButton = QtWidgets.QPushButton(self.frame_2)
        self.startPushButton.setObjectName("startPushButton")
        self.horizontalLayout.addWidget(self.startPushButton)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(75)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(2)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.horizontalLayout_21.addWidget(self.stackedWidget)
        self.verticalLayout_25.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem16)
        self.closeFigurePushButton = QtWidgets.QPushButton(self.frame_4)
        self.closeFigurePushButton.setObjectName("closeFigurePushButton")
        self.horizontalLayout_20.addWidget(self.closeFigurePushButton)
        self.addFigurePushButton = QtWidgets.QPushButton(self.frame_4)
        self.addFigurePushButton.setObjectName("addFigurePushButton")
        self.horizontalLayout_20.addWidget(self.addFigurePushButton)
        self.saveFigurePushButton = QtWidgets.QPushButton(self.frame_4)
        self.saveFigurePushButton.setObjectName("saveFigurePushButton")
        self.horizontalLayout_20.addWidget(self.saveFigurePushButton)
        self.figureToolButton = QtWidgets.QToolButton(self.frame_4)
        self.figureToolButton.setObjectName("figureToolButton")
        self.horizontalLayout_20.addWidget(self.figureToolButton)
        self.verticalLayout_25.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame)

        self.retranslateUi(branch)
        QtCore.QMetaObject.connectSlotsByName(branch)
        self.connect_actions()
        self.addEntryBox()
        self.addEntryBox()

    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addProteinPushButton.setText(_translate("Form", "Add Protein"))
        self.addTFPushButton.setText(_translate("Form", "Add TF"))
        self.addmRNAPushButton.setText(_translate("Form", "Add mRNA"))
        self.toolButton.setText(_translate("Form", "..."))
        self.label_26.setText(_translate("Form", "Trajectories"))
        self.label_25.setText(_translate("Form", "Steps"))
        self.startPushButton.setText(_translate("Form", "Start"))
        self.closeFigurePushButton.setText(_translate("Form", "Close Figure"))
        self.addFigurePushButton.setText(_translate("Form", "Add Figure"))
        self.saveFigurePushButton.setText(_translate("Form", "Save Figure"))
        self.figureToolButton.setText(_translate("Form", "..."))


    def connect_actions(self):
        """Connects Actions to the corresponding Commands"""
        self.startPushButton.clicked.connect(lambda : self.commands.start_default(
            self.parameters
            ))
        
        
        self.saveFigurePushButton.clicked.connect(self.commands.save_figure)
        self.closeFigurePushButton.clicked.connect(self.commands.close_figure)
        self.addFigurePushButton.clicked.connect(self.commands.add_figure)

        # -------------------------------------------------------------
        # Internal to this Widget and its children

        self.addProteinPushButton.clicked.connect(self.addEntryBox)

        pass


    def addEntryBox(self):
        
        var = EntryBox(self, len(self.entry_boxes))
        var.setupUi(self.scrollAreaWidgetContents_2)

        self.verticalLayout_12.addWidget(var.proteinGroupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_12.update()
        self.scrollArea.adjustSize()

        self.entry_boxes.append(var)


    def add_figure_to_display(self):
        pass


    @property
    def parameters(self):
        """returns the parameters required to run the analysis"""
        parameters = {}

        return parameters
    
    # ------------------------------------------------------------------
    # Events

    def _on_closing(self):
        """
        Called when the widget should be closed
        """
        pass

    def _on_EntryBox_removed(self, number):
        
        entry_boxes = []
        for index in len(self.entry_boxes):
            if index == number:

                self.scrollAreaWidgetContents_2.removeWidget()
                continue
                
            box = self.entry_boxes[index]
            box.index = len(entry_boxes)
            entry_boxes.append(box)
            continue

        self.entry_boxes = entry_boxes


