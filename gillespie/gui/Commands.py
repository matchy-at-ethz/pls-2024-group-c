import os
import random
import webbrowser

import requests
from PyQt5 import QtWidgets

from gillespie import get_package_root

from .util import DataStruct, PlotStruct

random.seed(1)


class CommandStruct:
    """
    Used to hold the Commands orginating from the GUI and other places.
    """

    def __init__(self, scene_tree):

        self.SceneTree = scene_tree

        pass

    def run_simulation(self, data: dict):
        print("io")
        data_struct = DataStruct(data)

        for i in range(0, data["steps"]):
            data_struct.update()

        plot_struct = PlotStruct(data_struct)
        name = f"a{random.randint(1, 1000)}b.png"
        path = get_package_root() / "assets" / name
        plot_struct.createPlotRandTraject(2, path)  # replace with correct name
        self.SceneTree.scenes[self.SceneTree.current_scene].add_image_page(
            name
        )  # display it
        pass

    def switchScene(self, scene: str):

        self.SceneTree.swich_scene(scene)
        pass

    def change_mode(self, scene: str):

        self.SceneTree.ModesPort.set_active(scene)
        pass

    def openConfig(self):
        pass

    def saveConfig(self):
        pass

    def save_figure(self):
        pass

    def close_figure(self):
        pass

    def add_figure(self):
        pass

    def add_preset(self, prefix: str):
        """
        Adds a set of parameters(path) to the navigator, not complete
        """
        text, ok = QtWidgets.QInputDialog.getText(
            self.SceneTree.MainWindow, "", "Enter Name:"
        )
        path = os.path.join(ROOT_DIR, f"Resources/ParameterSets/{prefix}/{text}")
        valid = self.verify_name(path)

        if not valid:
            reply = QtWidgets.QMessageBox.question(
                self.SceneTree.MainWindow,
                "",
                "Imvalid name, Would u lyke to retry?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No,
            )

            if reply == QtWidgets.QMessageBox.Yes:
                self.add_preset()
                return
            else:
                return

        self.create_preset_from_default(name=text, path=path)

        if ok == True:
            self.SceneTree.screen.add_preset(name=text, path=path)

        pass

    def verify_name(self, name: str):
        if name == "":
            return False
        return True

    def create_preset_from_default(self, name: str, path: str):
        """create the default preset and save it in the correct place"""
        pass

    def set_preset_active(self, name: str):
        """Loads a given set of parameters and then changes the hud values to it"""

        err = self.SceneTree.scenes[self.SceneTree.current_scene].load_parameters(
            name
        )  # load parameters do nothing except display a message if it fails
        if err:
            QtWidgets.QMessageBox.about(
                self.SceneTree.MainWindow,
                "Notification",
                "The selected Preset is Invalid! \n UwU",
            )
            return

        self.SceneTree.screen.change_activated_preset(
            name
        )  # Change the visual appearance in the GUI

        pass

    def remove_preset(self, name):

        reply = QtWidgets.QMessageBox.question(
            self.SceneTree.MainWindow,
            "Confirm",
            "Do you want to proceed?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No,
        )

        if reply == QtWidgets.QMessageBox.Yes:
            self.delete_preset()
            self.SceneTree.screen.remove_preset(name)
        else:
            return

    def load_parameters(self, path: str):
        pass

    def delete_preset(self):
        pass

    def exit(self):
        """Closes the application, Doesnt save the configurations"""
        self.SceneTree.MainWindow.close()
        pass

    def exportConfig(self, type: str):
        pass

    def open_url(self, url):
        """Open a Link in the default Browser

        Args:
            url(str):  Url which should be opened
        """
        try:
            # Open the URL in the default web browser
            webbrowser.open(url)
            print(f"Opening {url} in your browser...")
        except Exception as e:
            print(f"An error occurred while trying to open the URL: {e}")

    def loadWeb(self, url):
        """Load content from a given URL.

        Args:
            url(str):  Url which should be opened
        """
        try:
            # Make a GET request to the URL
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            response.raise_for_status()
            # Print or process the content of the response
            print("Content Loaded:")
            print(response.text)  # This will print the HTML content of the page
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Error occurred while requesting the URL: {req_err}")
