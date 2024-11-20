from qtpy import QtWidgets, QtGui, QtCore
from PIL import Image
from pathlib import Path
import os

from Projectconfiguration import ROOT_DIR, VERSION, NAME, LOADSCREEN_IMAGE

class LoadWindow(object):
    """
    THIS IS ATROCHIOUS DO NOT RESIZE AT ANY COST!!!!!
    """

    def __init__(self, scene_tree, MainWindow):
        super().__init__()
        self.scene_tree = scene_tree
        
        # Load and scale the image
        self.MainWindow = MainWindow
        self.MainWindow.setModal(True)
        image = Image.open(os.path.join(ROOT_DIR,f"Resources\{LOADSCREEN_IMAGE}"))
        new_size = (image.width // 2, image.height // 2)
        scaled_image = image.resize(new_size)

        # Convert PIL image to data that can be used with QPixmap
        # Convert to RGBA if not already, then save as bytes in PNG format
        byte_data = scaled_image.convert("RGBA").tobytes("raw", "RGBA")

        # Convert the image data into a QImage, then into a QPixmap
        qt_image = QtGui.QImage(byte_data, scaled_image.width, scaled_image.height, QtGui.QImage.Format_RGBA8888)
        pixmap = QtGui.QPixmap.fromImage(qt_image)

        # Configure window properties
        self.MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove window borders
        self.MainWindow.setFixedSize(new_size[0], new_size[1])  # Disable resizing
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Optional, for rounded corners or transparency
        
        # Center the window on screen
        x_position = (scene_tree.screen_width // 2) - (new_size[0] // 2)
        y_position = (scene_tree.screen_height // 2) - (new_size[1] // 2)
        self.MainWindow.move(x_position, y_position)

        # Set the background image
        self.label_image = QtWidgets.QLabel(self.MainWindow)
        self.label_image.setPixmap(pixmap)
        self.label_image.setGeometry(0, 0, new_size[0], new_size[1])
        self.label_image.backgroundColor = QtGui.QColor("#BE632E")
        
        # Add banner at the bottom of the image
        banner_height = int(new_size[1] * 0.2 +1)
        self.banner = QtWidgets.QFrame(self.MainWindow )
        self.banner.backgroundColor = QtGui.QColor("#BE632E")
        self.banner.setGeometry(0, int(new_size[1] * 0.8), new_size[0], banner_height)
        self.banner.setStyleSheet("background-color: #BE632E;")

        # Title label
        title_font = QtGui.QFont("Times", 30)
        self.title_label = QtWidgets.QLabel(NAME, self.banner)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet("color: white;")
        self.title_label.move(5, 5)

        # Version label
        version_font = QtGui.QFont("Helvetica", 8)
        self.version_label = QtWidgets.QLabel(f"Version {VERSION}", self.banner)
        self.version_label.setFont(version_font)
        self.version_label.setStyleSheet("color: white;")
        self.version_label.move(180, banner_height - 20)

        # Loading message
        load_message_font = QtGui.QFont("Helvetica", 10)
        self.load_message_label = QtWidgets.QLabel("Loading Data", self.banner)
        self.load_message_label.setFont(load_message_font)
        self.load_message_label.setStyleSheet("color: white;")
        self.load_message_label.wrap = True
        self.load_message_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.load_message_label.move(new_size[0] - 180, banner_height - 35)

        self.MainWindow.show()

        # Simulate loading process
        QtCore.QTimer.singleShot(1500, self.update_loading_message)  # Display "Loading Data" after 1.5 seconds
        QtCore.QTimer.singleShot(5500, self.finish_loading)  # Simulate finishing loading after 5 seconds

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def update_loading_message(self):
        self.load_message_label.setText("Initializing Modules...")

    def finish_loading(self):
        self.scene_tree.MainWindow.setWindowOpacity(1)
        self.MainWindow.close()  # Close the window after loading finishes
        pass

