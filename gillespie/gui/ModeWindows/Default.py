# -*- coding: utf-8 -*-
import os

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets

from gillespie import get_package_root


class DefaultScene(object):

    protein1_name = None
    Protein2_name = None

    def __init__(self, parent, commands):
        self.parent = parent
        self.commands = commands

        self.figures = []
        self.current_page = [0, None]

    def setupUi(self, branch):
        self.gridLayout = self.parent.gridLayout
        self.frame = QtWidgets.QFrame(branch)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(545, 700))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.proteinGroupBox = QtWidgets.QGroupBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(75)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(
            self.proteinGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.proteinGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.proteinGroupBox.setFont(font)
        self.proteinGroupBox.setObjectName("proteinGroupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.proteinGroupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.proteinGroupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.frame_8.setFont(font)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.frame_36 = QtWidgets.QFrame(self.frame_8)
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(4)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.nameComboBox1 = QtWidgets.QComboBox(self.frame_36)
        self.nameComboBox1.setObjectName("nameComboBox1")
        self.verticalLayout_26.addWidget(self.nameComboBox1)
        self.nameComboBox2 = QtWidgets.QComboBox(self.frame_36)
        self.nameComboBox2.setObjectName("nameComboBox2")
        self.verticalLayout_26.addWidget(self.nameComboBox2)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_26.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.frame_36)
        self.horizontalLayout_6.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.proteinGroupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.frame_9.setFont(font)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.frame_37 = QtWidgets.QFrame(self.frame_9)
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(4)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.cSpinBox1 = QtWidgets.QSpinBox(self.frame_37)
        self.cSpinBox1.setObjectName("cSpinBox1")
        self.verticalLayout_27.addWidget(self.cSpinBox1)
        self.cSpinBox1_2 = QtWidgets.QSpinBox(self.frame_37)
        self.cSpinBox1_2.setObjectName("cSpinBox1_2")
        self.verticalLayout_27.addWidget(self.cSpinBox1_2)
        self.verticalLayout_2.addWidget(self.frame_37)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_6.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.proteinGroupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.frame_10.setFont(font)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.frame_35 = QtWidgets.QFrame(self.frame_10)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(4)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.intjDDoubleSpinBox1 = QtWidgets.QDoubleSpinBox(self.frame_35)
        self.intjDDoubleSpinBox1.setObjectName("intjDDoubleSpinBox1")
        self.verticalLayout_23.addWidget(self.intjDDoubleSpinBox1)
        self.intjDDoubleSpinBox2 = QtWidgets.QDoubleSpinBox(self.frame_35)
        self.intjDDoubleSpinBox2.setObjectName("intjDDoubleSpinBox2")
        self.verticalLayout_23.addWidget(self.intjDDoubleSpinBox2)
        self.verticalLayout_4.addWidget(self.frame_35)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_6.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.proteinGroupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.frame_11.setFont(font)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_24.addWidget(self.label_7)
        self.frame_34 = QtWidgets.QFrame(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMinimumSize(QtCore.QSize(0, 46))
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tfRadioButton1 = QtWidgets.QRadioButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tfRadioButton1.sizePolicy().hasHeightForWidth()
        )
        self.tfRadioButton1.setSizePolicy(sizePolicy)
        self.tfRadioButton1.setText("")
        self.tfRadioButton1.setObjectName("tfRadioButton1")
        self.verticalLayout_5.addWidget(self.tfRadioButton1)
        self.tfRadioButton1_2 = QtWidgets.QRadioButton(self.frame_34)
        self.tfRadioButton1_2.setText("")
        self.tfRadioButton1_2.setObjectName("tfRadioButton1_2")
        self.verticalLayout_5.addWidget(self.tfRadioButton1_2)
        self.verticalLayout_24.addWidget(self.frame_34)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_24.addItem(spacerItem3)
        self.horizontalLayout_6.addWidget(self.frame_11)
        self.verticalLayout_41.addWidget(self.proteinGroupBox)
        self.mrnaGroupBox = QtWidgets.QGroupBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(35)
        sizePolicy.setHeightForWidth(self.mrnaGroupBox.sizePolicy().hasHeightForWidth())
        self.mrnaGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mrnaGroupBox.setFont(font)
        self.mrnaGroupBox.setObjectName("mrnaGroupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.mrnaGroupBox)
        self.horizontalLayout_7.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_12 = QtWidgets.QFrame(self.mrnaGroupBox)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.frame_30 = QtWidgets.QFrame(self.frame_12)
        self.frame_30.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_30.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.mRNANameComboBox1 = QtWidgets.QComboBox(self.frame_30)
        self.mRNANameComboBox1.setObjectName("mRNANameComboBox1")
        self.verticalLayout_19.addWidget(self.mRNANameComboBox1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_19.addItem(spacerItem4)
        self.verticalLayout_6.addWidget(self.frame_30)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_6.addItem(spacerItem5)
        self.frame_31 = QtWidgets.QFrame(self.frame_12)
        self.frame_31.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_31.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.mRNANameComboBox1_2 = QtWidgets.QComboBox(self.frame_31)
        self.mRNANameComboBox1_2.setObjectName("mRNANameComboBox1_2")
        self.verticalLayout_20.addWidget(self.mRNANameComboBox1_2)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_20.addItem(spacerItem6)
        self.verticalLayout_6.addWidget(self.frame_31)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_7.addWidget(self.frame_12)
        self.frame_15 = QtWidgets.QFrame(self.mrnaGroupBox)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_9 = QtWidgets.QLabel(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_18.addWidget(self.label_9)
        self.frame_7 = QtWidgets.QFrame(self.frame_15)
        self.frame_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.mRNAEncodeComboBox1 = QtWidgets.QComboBox(self.frame_7)
        self.mRNAEncodeComboBox1.setObjectName("mRNAEncodeComboBox1")
        self.verticalLayout_7.addWidget(self.mRNAEncodeComboBox1)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_7.addItem(spacerItem8)
        self.verticalLayout_18.addWidget(self.frame_7)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_18.addItem(spacerItem9)
        self.frame_27 = QtWidgets.QFrame(self.frame_15)
        self.frame_27.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_27.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.mRNAEncodeComboBox2 = QtWidgets.QComboBox(self.frame_27)
        self.mRNAEncodeComboBox2.setObjectName("mRNAEncodeComboBox2")
        self.verticalLayout_17.addWidget(self.mRNAEncodeComboBox2)
        spacerItem10 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_17.addItem(spacerItem10)
        self.verticalLayout_18.addWidget(self.frame_27)
        spacerItem11 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_18.addItem(spacerItem11)
        self.horizontalLayout_7.addWidget(self.frame_15)
        self.frame_13 = QtWidgets.QFrame(self.mrnaGroupBox)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_10 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_16.addWidget(self.label_10)
        self.frame_5 = QtWidgets.QFrame(self.frame_13)
        self.frame_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mRNAConcSpinBox1 = QtWidgets.QSpinBox(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mRNAConcSpinBox1.sizePolicy().hasHeightForWidth()
        )
        self.mRNAConcSpinBox1.setSizePolicy(sizePolicy)
        self.mRNAConcSpinBox1.setObjectName("mRNAConcSpinBox1")
        self.verticalLayout.addWidget(self.mRNAConcSpinBox1)
        spacerItem12 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem12)
        self.verticalLayout_16.addWidget(self.frame_5)
        spacerItem13 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_16.addItem(spacerItem13)
        self.frame_6 = QtWidgets.QFrame(self.frame_13)
        self.frame_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.mRNAConcSpinBox1_2 = QtWidgets.QSpinBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mRNAConcSpinBox1_2.sizePolicy().hasHeightForWidth()
        )
        self.mRNAConcSpinBox1_2.setSizePolicy(sizePolicy)
        self.mRNAConcSpinBox1_2.setObjectName("mRNAConcSpinBox1_2")
        self.verticalLayout_8.addWidget(self.mRNAConcSpinBox1_2)
        spacerItem14 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_8.addItem(spacerItem14)
        self.verticalLayout_16.addWidget(self.frame_6)
        spacerItem15 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_16.addItem(spacerItem15)
        self.horizontalLayout_7.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.mrnaGroupBox)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.frame_19 = QtWidgets.QFrame(self.frame_14)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(4)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_18 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_23 = QtWidgets.QFrame(self.frame_18)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(12)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.mRNAParamLabel1A = QtWidgets.QLabel(self.frame_23)
        self.mRNAParamLabel1A.setObjectName("mRNAParamLabel1A")
        self.horizontalLayout_12.addWidget(self.mRNAParamLabel1A)
        self.mRNAParamDoubleSpinBox1A = QtWidgets.QDoubleSpinBox(self.frame_23)
        self.mRNAParamDoubleSpinBox1A.setObjectName("mRNAParamDoubleSpinBox1A")
        self.horizontalLayout_12.addWidget(self.mRNAParamDoubleSpinBox1A)
        self.verticalLayout_12.addWidget(self.frame_23)
        self.frame_24 = QtWidgets.QFrame(self.frame_18)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.mRNAParamLabel1B = QtWidgets.QLabel(self.frame_24)
        self.mRNAParamLabel1B.setObjectName("mRNAParamLabel1B")
        self.horizontalLayout_13.addWidget(self.mRNAParamLabel1B)
        self.mRNAParamDoubleSpinBox1B = QtWidgets.QDoubleSpinBox(self.frame_24)
        self.mRNAParamDoubleSpinBox1B.setObjectName("mRNAParamDoubleSpinBox1B")
        self.horizontalLayout_13.addWidget(self.mRNAParamDoubleSpinBox1B)
        self.verticalLayout_12.addWidget(self.frame_24)
        self.verticalLayout_13.addWidget(self.frame_18)
        spacerItem16 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_13.addItem(spacerItem16)
        self.frame_17 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_22 = QtWidgets.QFrame(self.frame_17)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.mRNAParamLabel2A = QtWidgets.QLabel(self.frame_22)
        self.mRNAParamLabel2A.setObjectName("mRNAParamLabel2A")
        self.horizontalLayout_11.addWidget(self.mRNAParamLabel2A)
        self.mRNAParamDoubleSpinBox2A = QtWidgets.QDoubleSpinBox(self.frame_22)
        self.mRNAParamDoubleSpinBox2A.setObjectName("mRNAParamDoubleSpinBox2A")
        self.horizontalLayout_11.addWidget(self.mRNAParamDoubleSpinBox2A)
        self.verticalLayout_10.addWidget(self.frame_22)
        self.frame_21 = QtWidgets.QFrame(self.frame_17)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.mRNAParamLabel2B = QtWidgets.QLabel(self.frame_21)
        self.mRNAParamLabel2B.setObjectName("mRNAParamLabel2B")
        self.horizontalLayout_10.addWidget(self.mRNAParamLabel2B)
        self.mRNAParamDoubleSpinBox2B = QtWidgets.QDoubleSpinBox(self.frame_21)
        self.mRNAParamDoubleSpinBox2B.setObjectName("mRNAParamDoubleSpinBox2B")
        self.horizontalLayout_10.addWidget(self.mRNAParamDoubleSpinBox2B)
        self.verticalLayout_10.addWidget(self.frame_21)
        self.verticalLayout_13.addWidget(self.frame_17)
        spacerItem17 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_13.addItem(spacerItem17)
        self.verticalLayout_9.addWidget(self.frame_19)
        self.horizontalLayout_7.addWidget(self.frame_14)
        self.frame_16 = QtWidgets.QFrame(self.mrnaGroupBox)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.mRNALabel = QtWidgets.QLabel(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mRNALabel.sizePolicy().hasHeightForWidth())
        self.mRNALabel.setSizePolicy(sizePolicy)
        self.mRNALabel.setObjectName("mRNALabel")
        self.verticalLayout_22.addWidget(self.mRNALabel)
        self.frame_33 = QtWidgets.QFrame(self.frame_16)
        self.frame_33.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_33.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.mRNATBDDoubleSpinBox1 = QtWidgets.QSpinBox(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mRNATBDDoubleSpinBox1.sizePolicy().hasHeightForWidth()
        )
        self.mRNATBDDoubleSpinBox1.setSizePolicy(sizePolicy)
        self.mRNATBDDoubleSpinBox1.setObjectName("mRNATBDDoubleSpinBox1")
        self.verticalLayout_21.addWidget(self.mRNATBDDoubleSpinBox1)
        spacerItem18 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_21.addItem(spacerItem18)
        self.verticalLayout_22.addWidget(self.frame_33)
        spacerItem19 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_22.addItem(spacerItem19)
        self.frame_32 = QtWidgets.QFrame(self.frame_16)
        self.frame_32.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_32.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.mRNATBDDoubleSpinBox2 = QtWidgets.QSpinBox(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mRNATBDDoubleSpinBox2.sizePolicy().hasHeightForWidth()
        )
        self.mRNATBDDoubleSpinBox2.setSizePolicy(sizePolicy)
        self.mRNATBDDoubleSpinBox2.setObjectName("mRNATBDDoubleSpinBox2")
        self.verticalLayout_11.addWidget(self.mRNATBDDoubleSpinBox2)
        spacerItem20 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_11.addItem(spacerItem20)
        self.verticalLayout_22.addWidget(self.frame_32)
        spacerItem21 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_22.addItem(spacerItem21)
        self.horizontalLayout_7.addWidget(self.frame_16)
        self.verticalLayout_41.addWidget(self.mrnaGroupBox)
        self.widget = QtWidgets.QWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(4)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.ParameterGroupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(55)
        sizePolicy.setHeightForWidth(
            self.ParameterGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.ParameterGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ParameterGroupBox.setFont(font)
        self.ParameterGroupBox.setObjectName("ParameterGroupBox")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.ParameterGroupBox)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_38 = QtWidgets.QFrame(self.ParameterGroupBox)
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label1 = QtWidgets.QLabel(self.frame_38)
        self.label1.setObjectName("label1")
        self.horizontalLayout_3.addWidget(self.label1)
        spacerItem22 = QtWidgets.QSpacerItem(
            59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem22)
        self.label1ComboBox = QtWidgets.QComboBox(self.frame_38)
        self.label1ComboBox.setObjectName("label1ComboBox")
        self.horizontalLayout_3.addWidget(self.label1ComboBox)
        self.verticalLayout_15.addWidget(self.frame_38)
        self.frame_39 = QtWidgets.QFrame(self.ParameterGroupBox)
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_39)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label2 = QtWidgets.QLabel(self.frame_39)
        self.label2.setObjectName("label2")
        self.horizontalLayout_4.addWidget(self.label2)
        spacerItem23 = QtWidgets.QSpacerItem(
            62, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem23)
        self.label2ComboBox = QtWidgets.QComboBox(self.frame_39)
        self.label2ComboBox.setObjectName("label2ComboBox")
        self.horizontalLayout_4.addWidget(self.label2ComboBox)
        self.verticalLayout_15.addWidget(self.frame_39)
        self.frame_40 = QtWidgets.QFrame(self.ParameterGroupBox)
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_40)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label3 = QtWidgets.QLabel(self.frame_40)
        self.label3.setObjectName("label3")
        self.horizontalLayout_5.addWidget(self.label3)
        spacerItem24 = QtWidgets.QSpacerItem(
            62, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem24)
        self.label3SpinBox = QtWidgets.QSpinBox(self.frame_40)
        self.label3SpinBox.setObjectName("label3SpinBox")
        self.horizontalLayout_5.addWidget(self.label3SpinBox)
        self.verticalLayout_15.addWidget(self.frame_40)
        self.frame_41 = QtWidgets.QFrame(self.ParameterGroupBox)
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label4 = QtWidgets.QLabel(self.frame_41)
        self.label4.setObjectName("label4")
        self.horizontalLayout_8.addWidget(self.label4)
        spacerItem25 = QtWidgets.QSpacerItem(
            62, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_8.addItem(spacerItem25)
        self.label4doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame_41)
        self.label4doubleSpinBox.setObjectName("label4doubleSpinBox")
        self.horizontalLayout_8.addWidget(self.label4doubleSpinBox)
        self.verticalLayout_15.addWidget(self.frame_41)
        self.frame_42 = QtWidgets.QFrame(self.ParameterGroupBox)
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_42)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label5 = QtWidgets.QLabel(self.frame_42)
        self.label5.setObjectName("label5")
        self.horizontalLayout_9.addWidget(self.label5)
        spacerItem26 = QtWidgets.QSpacerItem(
            62, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_9.addItem(spacerItem26)
        self.label5doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame_42)
        self.label5doubleSpinBox.setObjectName("label5doubleSpinBox")
        self.horizontalLayout_9.addWidget(self.label5doubleSpinBox)
        self.verticalLayout_15.addWidget(self.frame_42)
        self.frame_43 = QtWidgets.QFrame(self.ParameterGroupBox)
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(4)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label6 = QtWidgets.QLabel(self.frame_43)
        self.label6.setObjectName("label6")
        self.horizontalLayout_18.addWidget(self.label6)
        spacerItem27 = QtWidgets.QSpacerItem(
            62, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_18.addItem(spacerItem27)
        self.label6doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame_43)
        self.label6doubleSpinBox.setObjectName("label6doubleSpinBox")
        self.horizontalLayout_18.addWidget(self.label6doubleSpinBox)
        self.verticalLayout_15.addWidget(self.frame_43)
        self.frame_44 = QtWidgets.QFrame(self.ParameterGroupBox)
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_44)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(4)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label7 = QtWidgets.QLabel(self.frame_44)
        self.label7.setObjectName("label7")
        self.horizontalLayout_19.addWidget(self.label7)
        spacerItem28 = QtWidgets.QSpacerItem(
            62, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_19.addItem(spacerItem28)
        self.label7ComboBox = QtWidgets.QComboBox(self.frame_44)
        self.label7ComboBox.setObjectName("label7ComboBox")
        self.horizontalLayout_19.addWidget(self.label7ComboBox)
        self.verticalLayout_15.addWidget(self.frame_44)
        self.horizontalLayout_14.addWidget(self.ParameterGroupBox)
        self.transcriptionFactorsGroupBox = QtWidgets.QGroupBox(self.widget)
        self.transcriptionFactorsGroupBox.setObjectName("transcriptionFactorsGroupBox")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(
            self.transcriptionFactorsGroupBox
        )
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_20 = QtWidgets.QFrame(self.transcriptionFactorsGroupBox)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_20 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_28.addWidget(self.label_20)
        self.frame_45 = QtWidgets.QFrame(self.frame_20)
        self.frame_45.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy)
        self.frame_45.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_45.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_45)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.tfNameComboBox1 = QtWidgets.QComboBox(self.frame_45)
        self.tfNameComboBox1.setObjectName("tfNameComboBox1")
        self.verticalLayout_29.addWidget(self.tfNameComboBox1)
        spacerItem29 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_29.addItem(spacerItem29)
        self.verticalLayout_28.addWidget(self.frame_45)
        spacerItem30 = QtWidgets.QSpacerItem(
            20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_28.addItem(spacerItem30)
        self.frame_46 = QtWidgets.QFrame(self.frame_20)
        self.frame_46.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy)
        self.frame_46.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_46.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_46)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.tfNameComboBox2 = QtWidgets.QComboBox(self.frame_46)
        self.tfNameComboBox2.setObjectName("tfNameComboBox2")
        self.verticalLayout_30.addWidget(self.tfNameComboBox2)
        spacerItem31 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_30.addItem(spacerItem31)
        self.verticalLayout_28.addWidget(self.frame_46)
        spacerItem32 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_28.addItem(spacerItem32)
        self.horizontalLayout_15.addWidget(self.frame_20)
        self.frame_25 = QtWidgets.QFrame(self.transcriptionFactorsGroupBox)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_21 = QtWidgets.QLabel(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_31.addWidget(self.label_21)
        self.frame_26 = QtWidgets.QFrame(self.frame_25)
        self.frame_26.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_26.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.tfEncodesComboBox1 = QtWidgets.QComboBox(self.frame_26)
        self.tfEncodesComboBox1.setObjectName("tfEncodesComboBox1")
        self.verticalLayout_32.addWidget(self.tfEncodesComboBox1)
        spacerItem33 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_32.addItem(spacerItem33)
        self.verticalLayout_31.addWidget(self.frame_26)
        spacerItem34 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_31.addItem(spacerItem34)
        self.frame_28 = QtWidgets.QFrame(self.frame_25)
        self.frame_28.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.tfEncodesComboBox2 = QtWidgets.QComboBox(self.frame_28)
        self.tfEncodesComboBox2.setObjectName("tfEncodesComboBox2")
        self.verticalLayout_33.addWidget(self.tfEncodesComboBox2)
        spacerItem35 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_33.addItem(spacerItem35)
        self.verticalLayout_31.addWidget(self.frame_28)
        spacerItem36 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_31.addItem(spacerItem36)
        self.horizontalLayout_15.addWidget(self.frame_25)
        self.frame_29 = QtWidgets.QFrame(self.transcriptionFactorsGroupBox)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.label_23 = QtWidgets.QLabel(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_34.addWidget(self.label_23)
        self.frame_47 = QtWidgets.QFrame(self.frame_29)
        self.frame_47.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy)
        self.frame_47.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_47.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_47)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.tfConcSpinBox1 = QtWidgets.QSpinBox(self.frame_47)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tfConcSpinBox1.sizePolicy().hasHeightForWidth()
        )
        self.tfConcSpinBox1.setSizePolicy(sizePolicy)
        self.tfConcSpinBox1.setObjectName("tfConcSpinBox1")
        self.verticalLayout_35.addWidget(self.tfConcSpinBox1)
        spacerItem37 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_35.addItem(spacerItem37)
        self.verticalLayout_34.addWidget(self.frame_47)
        spacerItem38 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_34.addItem(spacerItem38)
        self.frame_48 = QtWidgets.QFrame(self.frame_29)
        self.frame_48.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy)
        self.frame_48.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_48.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.frame_48)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.tfConcSpinBox2 = QtWidgets.QSpinBox(self.frame_48)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tfConcSpinBox2.sizePolicy().hasHeightForWidth()
        )
        self.tfConcSpinBox2.setSizePolicy(sizePolicy)
        self.tfConcSpinBox2.setObjectName("tfConcSpinBox2")
        self.verticalLayout_36.addWidget(self.tfConcSpinBox2)
        spacerItem39 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_36.addItem(spacerItem39)
        self.verticalLayout_34.addWidget(self.frame_48)
        spacerItem40 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_34.addItem(spacerItem40)
        self.horizontalLayout_15.addWidget(self.frame_29)
        self.frame_49 = QtWidgets.QFrame(self.transcriptionFactorsGroupBox)
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_49)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.tfLabel4 = QtWidgets.QLabel(self.frame_49)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tfLabel4.sizePolicy().hasHeightForWidth())
        self.tfLabel4.setSizePolicy(sizePolicy)
        self.tfLabel4.setObjectName("tfLabel4")
        self.verticalLayout_37.addWidget(self.tfLabel4)
        self.frame_50 = QtWidgets.QFrame(self.frame_49)
        self.frame_50.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy)
        self.frame_50.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_50.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_50)
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.tfTBDSpinBox1 = QtWidgets.QDoubleSpinBox(self.frame_50)
        self.tfTBDSpinBox1.setObjectName("tfTBDSpinBox1")
        self.verticalLayout_38.addWidget(self.tfTBDSpinBox1)
        spacerItem41 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_38.addItem(spacerItem41)
        self.verticalLayout_37.addWidget(self.frame_50)
        spacerItem42 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_37.addItem(spacerItem42)
        self.frame_51 = QtWidgets.QFrame(self.frame_49)
        self.frame_51.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy)
        self.frame_51.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_51.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.tfTBDSpinBox1_2 = QtWidgets.QDoubleSpinBox(self.frame_51)
        self.tfTBDSpinBox1_2.setObjectName("tfTBDSpinBox1_2")
        self.verticalLayout_39.addWidget(self.tfTBDSpinBox1_2)
        spacerItem43 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_39.addItem(spacerItem43)
        self.verticalLayout_37.addWidget(self.frame_51)
        spacerItem44 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_37.addItem(spacerItem44)
        self.horizontalLayout_15.addWidget(self.frame_49)
        self.horizontalLayout_14.addWidget(self.transcriptionFactorsGroupBox)
        self.verticalLayout_41.addWidget(self.widget)
        spacerItem45 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_41.addItem(spacerItem45)
        self.frame_52 = QtWidgets.QFrame(self.frame_3)
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_52)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(4)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_52)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
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
        spacerItem46 = QtWidgets.QSpacerItem(
            424, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_17.addItem(spacerItem46)
        self.label_26 = QtWidgets.QLabel(self.frame_54)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_17.addWidget(self.label_26)
        spacerItem47 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_17.addItem(spacerItem47)
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
        spacerItem48 = QtWidgets.QSpacerItem(
            419, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_16.addItem(spacerItem48)
        self.label_25 = QtWidgets.QLabel(self.frame_53)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_16.addWidget(self.label_25)
        spacerItem49 = QtWidgets.QSpacerItem(
            40, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_16.addItem(spacerItem49)
        self.stepsSpinBox = QtWidgets.QSpinBox(self.frame_53)
        self.stepsSpinBox.setObjectName("stepsSpinBox")
        self.horizontalLayout_16.addWidget(self.stepsSpinBox)
        self.verticalLayout_14.addWidget(self.frame_53)
        self.verticalLayout_40.addWidget(self.groupBox_5)
        self.verticalLayout_41.addWidget(self.frame_52)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
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
        spacerItem50 = QtWidgets.QSpacerItem(
            427, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem50)
        self.startPushButton = QtWidgets.QPushButton(self.frame_2)
        self.startPushButton.setObjectName("startPushButton")
        self.horizontalLayout.addWidget(self.startPushButton)
        self.verticalLayout_41.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
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
        self.horizontalLayout_21.addWidget(self.stackedWidget)
        self.create_navigation_buttons()
        self.verticalLayout_25.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem51 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_20.addItem(spacerItem51)
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
        self.add_image_page("Panda.png.jpg")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.proteinGroupBox.setTitle(_translate("Form", "Protein"))
        self.label_4.setText(_translate("Form", "Name"))
        self.label_5.setText(_translate("Form", "am. initial"))
        self.label_6.setText(_translate("Form", "Intj"))
        self.label_7.setText(_translate("Form", "Transcription Factor"))
        self.mrnaGroupBox.setTitle(_translate("Form", "mRNA"))
        self.label_8.setText(_translate("Form", "Name"))
        self.label_9.setText(_translate("Form", "Encodes"))
        self.label_10.setText(_translate("Form", "am. initial"))
        self.label_11.setText(_translate("Form", "parameters"))
        self.mRNAParamLabel1A.setText(_translate("Form", "TextLabel"))
        self.mRNAParamLabel1B.setText(_translate("Form", "TextLabel"))
        self.mRNAParamLabel2A.setText(_translate("Form", "TextLabel"))
        self.mRNAParamLabel2B.setText(_translate("Form", "TextLabel"))
        self.mRNALabel.setText(_translate("Form", "Decayrate"))
        self.ParameterGroupBox.setTitle(_translate("Form", "GroupBoxName1"))
        self.label1.setText(_translate("Form", "Parameter1"))
        self.label2.setText(_translate("Form", "Parameter2"))
        self.label3.setText(_translate("Form", "complexform."))
        self.label4.setText(_translate("Form", "Dissociat."))
        self.label5.setText(_translate("Form", "Parameter5"))
        self.label6.setText(_translate("Form", "Parameter6"))
        self.label7.setText(_translate("Form", "Parameter7"))
        self.transcriptionFactorsGroupBox.setTitle(
            _translate("Form", "Transcription Factors")
        )
        self.label_20.setText(_translate("Form", "Name"))
        self.label_21.setText(_translate("Form", "Encodes"))
        self.label_23.setText(_translate("Form", "am. initial"))
        self.tfLabel4.setText(_translate("Form", "Decayrate"))
        self.label_26.setText(_translate("Form", "Trajectories"))
        self.label_25.setText(_translate("Form", "Steps"))
        self.startPushButton.setText(_translate("Form", "Start"))
        self.closeFigurePushButton.setText(_translate("Form", "Close Figure"))
        self.addFigurePushButton.setText(_translate("Form", "Add Figure"))
        self.saveFigurePushButton.setText(_translate("Form", "Save Figure"))
        self.figureToolButton.setText(_translate("Form", "..."))

    # ================================================================================
    # Dont overwrite when copying (below)

    def connect_actions(self):
        """Connects Actions to the corresponding Commands"""
        print("io")
        self.startPushButton.clicked.connect(
            lambda: self.commands.run_simulation(self.parameters)
        )

        self.saveFigurePushButton.clicked.connect(self.commands.save_figure)
        self.closeFigurePushButton.clicked.connect(self.commands.close_figure)
        self.addFigurePushButton.clicked.connect(self.commands.add_figure)
        pass

    def create_navigation_buttons(self):
        """Create next and previous buttons and place them in the upper-right corner."""
        self.nav_widget = QtWidgets.QWidget(self.frame)
        self.nav_layout = QtWidgets.QHBoxLayout(self.nav_widget)
        self.nav_layout.setContentsMargins(0, 0, 0, 0)
        self.nav_layout.addStretch()

        # Previous button
        self.prev_button = QtWidgets.QPushButton("◄", self.frame)
        self.prev_button.setFixedSize(30, 30)
        self.prev_button.clicked.connect(self.previous_page)
        self.nav_layout.addWidget(self.prev_button)

        # Next button
        self.next_button = QtWidgets.QPushButton("►", self.frame)
        self.next_button.setFixedSize(30, 30)
        self.next_button.clicked.connect(self.next_page)
        self.nav_layout.addWidget(self.next_button)

        # Add the navigation layout to the stacked widget
        self.verticalLayout_25.addWidget(
            self.nav_widget, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignRight
        )

    def add_image_page(self, image_name):
        # Load image using PIL
        image_path = get_package_root() / "assets" / image_name

        image = Image.open(image_path)
        qt_image = self.pil_to_qt_image(image)

        # Create a new widget for the page
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)

        # QLabel to hold the image
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        label_image = QtWidgets.QLabel(page)
        label_image.setAlignment(QtCore.Qt.AlignCenter)
        label_image.setSizePolicy(sizePolicy)
        layout.addWidget(label_image)

        # Scale and set the image
        self.scale_and_set_pixmap(label_image, qt_image, scale=page.size())

        # Add the page to the stacked widget
        self.stackedWidget.addWidget(page)
        self.stackedWidget.setCurrentWidget(page)

    def pil_to_qt_image(self, pil_image):
        pil_image = pil_image.convert("RGBA")
        data = pil_image.tobytes("raw", "RGBA")
        qt_image = QtGui.QImage(
            data, pil_image.width, pil_image.height, QtGui.QImage.Format_RGBA8888
        )
        return qt_image

    def scale_and_set_pixmap(self, label, qt_image, scale):
        # Scale the pixmap to fit the stacked widget while maintaining aspect ratio
        pixmap = QtGui.QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(
            scale, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation
        )
        label.setPixmap(scaled_pixmap)

    @property
    def parameters(self):
        """Gather the Parameters and saves them in a fiel and then returns the Path to the file"""
        parameters = {
            "protein": {
                "1": {
                    "init": self.cSpinBox1.value(),
                    "decay": self.intjDDoubleSpinBox1.value(),
                },
                "2": {
                    "init": self.cSpinBox1.value(),
                    "decay": self.intjDDoubleSpinBox1.value(),
                },
            },
            "mRNA": {
                "mirna": {
                    "init": self.mRNAConcSpinBox1.value(),
                    "decay": self.mRNATBDDoubleSpinBox1.value(),
                    "alpha_s": self.mRNAParamDoubleSpinBox1A.value(),
                    "ks": self.mRNAParamDoubleSpinBox1B.value(),
                },
                "tmRNA": {
                    "init": self.mRNAConcSpinBox1_2.value(),
                    "decay": self.mRNATBDDoubleSpinBox2.value(),
                    "alpha_s": self.mRNAParamDoubleSpinBox2A.value(),
                    "ks": self.mRNAParamDoubleSpinBox2B.value(),
                },
            },
            "TF": {
                "init": self.mRNAConcSpinBox1_2.value(),
                "decay": self.mRNATBDDoubleSpinBox2.value(),
                "alpha_s": self.mRNAParamDoubleSpinBox2A.value(),
            },
            "beta": self.label3SpinBox.value(),
            "muc": self.label4doubleSpinBox.value(),
            "pir": self.label5doubleSpinBox.value(),
            "trajectories": self.trajectoriesSpinBox.value(),
            "steps": self.stepsSpinBox.value(),
        }

        return parameters

    # ------------------------------------------------------------------
    # Events

    def _on_closing(self):
        """
        Called when the widget should be closed
        """
        pass

    def next_page(self):
        """Go to the next page in the stacked widget."""
        current_index = self.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(next_index)

    def previous_page(self):
        """Go to the previous page in the stacked widget."""
        current_index = self.stackedWidget.currentIndex()
        prev_index = (
            current_index - 1 + self.stackedWidget.count()
        ) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(prev_index)

    def load_parameters(self, name: int):
        """Load preset given by the path and returns error if invalid"""
        return False
