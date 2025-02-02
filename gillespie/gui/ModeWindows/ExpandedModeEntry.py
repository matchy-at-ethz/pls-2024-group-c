# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class EntryBox(object):

    def __init__(self, parent, index):
        self.parent = parent
        self.index = index

    def setupUi(self, Form):

        self.proteinGroupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proteinGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.proteinGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.proteinGroupBox.setFont(font)
        self.proteinGroupBox.setTitle("")
        self.proteinGroupBox.setObjectName("proteinGroupBox")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.proteinGroupBox)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.proteinGroupBox)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setObjectName("label")
        self.horizontalLayout_13.addWidget(self.label)
        self.NameComboBox = QtWidgets.QComboBox(self.frame_6)
        self.NameComboBox.setEditable(True)
        self.NameComboBox.setObjectName("NameComboBox")
        self.horizontalLayout_13.addWidget(self.NameComboBox)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.proteinGroupBox)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_14.addWidget(self.label_2)
        self.cComboBox = QtWidgets.QComboBox(self.frame_7)
        self.cComboBox.setEditable(True)
        self.cComboBox.setObjectName("cComboBox")
        self.horizontalLayout_14.addWidget(self.cComboBox)
        self.verticalLayout.addWidget(self.frame_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.proteinGroupBox)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.decayRateDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.proteinGroupBox)
        self.decayRateDoubleSpinBox.setObjectName("decayRateDoubleSpinBox")
        self.horizontalLayout_10.addWidget(self.decayRateDoubleSpinBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.proteinGroupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.CreateDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.proteinGroupBox)
        self.CreateDoubleSpinBox.setObjectName("CreateDoubleSpinBox")
        self.horizontalLayout_11.addWidget(self.CreateDoubleSpinBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_15.addItem(spacerItem)
        self.removePushButton = QtWidgets.QPushButton(self.proteinGroupBox)
        self.removePushButton.setObjectName("removePushButton")
        self.horizontalLayout_15.addWidget(self.removePushButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.proteinGroupBox)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem2)
        self.tfRadioButton = QtWidgets.QRadioButton(self.frame_8)
        self.tfRadioButton.setText("")
        self.tfRadioButton.setObjectName("tfRadioButton")
        self.horizontalLayout_4.addWidget(self.tfRadioButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.targetComboBox = QtWidgets.QComboBox(self.frame_8)
        self.targetComboBox.setObjectName("targetComboBox")
        self.horizontalLayout_5.addWidget(self.targetComboBox)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem3)
        self.removeTFPushButton = QtWidgets.QPushButton(self.frame_8)
        self.removeTFPushButton.setObjectName("removeTFPushButton")
        self.horizontalLayout_5.addWidget(self.removeTFPushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem4)
        self.comboBox = QtWidgets.QComboBox(self.frame_8)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_6.addWidget(self.comboBox)
        self.betaSpinBox = QtWidgets.QDoubleSpinBox(self.frame_8)
        self.betaSpinBox.setObjectName("betaSpinBox")
        self.horizontalLayout_6.addWidget(self.betaSpinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_7.addItem(spacerItem5)
        self.addTargetPushButton = QtWidgets.QPushButton(self.frame_8)
        self.addTargetPushButton.setObjectName("addTargetPushButton")
        self.horizontalLayout_7.addWidget(self.addTargetPushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.line = QtWidgets.QFrame(self.proteinGroupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.frame_9 = QtWidgets.QFrame(self.proteinGroupBox)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_8.addItem(spacerItem6)
        self.mRNARadioButton = QtWidgets.QRadioButton(self.frame_9)
        self.mRNARadioButton.setText("")
        self.mRNARadioButton.setObjectName("mRNARadioButton")
        self.horizontalLayout_8.addWidget(self.mRNARadioButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.targetComboBox_2 = QtWidgets.QComboBox(self.frame_9)
        self.targetComboBox_2.setObjectName("targetComboBox_2")
        self.horizontalLayout_9.addWidget(self.targetComboBox_2)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_9.addItem(spacerItem7)
        self.removemRNAPushButton = QtWidgets.QPushButton(self.frame_9)
        self.removemRNAPushButton.setObjectName("removemRNAPushButton")
        self.horizontalLayout_9.addWidget(self.removemRNAPushButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_18.addItem(spacerItem8)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_9)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_18.addWidget(self.comboBox_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame_9)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_18.addWidget(self.doubleSpinBox)
        self.verticalLayout_11.addLayout(self.horizontalLayout_18)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_19.addItem(spacerItem9)
        self.addTargetPushButton_2 = QtWidgets.QPushButton(self.frame_9)
        self.addTargetPushButton_2.setObjectName("addTargetPushButton_2")
        self.horizontalLayout_19.addWidget(self.addTargetPushButton_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_19)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_4.addWidget(self.frame_9)
        self.horizontalLayout_12.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name"))
        self.label_2.setText(_translate("Form", "[c] Initial"))
        self.label_4.setText(_translate("Form", "Decay Rate"))
        self.label_9.setText(_translate("Form", "Unspecified Production"))
        self.removePushButton.setText(_translate("Form", "Remove"))
        self.label_5.setText(_translate("Form", "Transcription Factor"))
        self.label_6.setText(_translate("Form", "Target"))
        self.removeTFPushButton.setText(_translate("Form", "Remove"))
        self.addTargetPushButton.setText(_translate("Form", "Add Target"))
        self.label_7.setText(_translate("Form", "mRNA"))
        self.label_8.setText(_translate("Form", "Target"))
        self.removemRNAPushButton.setText(_translate("Form", "Remove"))
        self.addTargetPushButton_2.setText(_translate("Form", "Add Target"))

    def connect_actions(self):
        """Connects Actions to the corresponding Commands"""

        # -------------------------------------------------------------
        # Internal to this Widget and its children

        self.removePushButton.clicked.connect(self._on_closing)

        pass

    @property
    def parameters(self):
        """returns the parameters required to run the analysis"""
        parameters = {}

        return parameters

    # ------------------------------------------------------------------
    # Events

    def _on_closing(self, number):

        self.parent._on_EntryBox_removed(self.index)
