import requests
import webbrowser

class CommandStruct:
    """
    Used to hold the Commands orginating from the GUI.
    """

    def __init__(self, scene_tree):

        self.SceneTree = scene_tree

        pass


    def switchScene(self, scene : str):
        pass

    def change_mode(self, scene : str):

        self.SceneTree.ModesPort.set_active(scene)
        pass


    def openConfig(self):
         pass
    

    def saveConfig(self):
         pass
    

    def exportConfig(self, type : str):
         pass
    

    def open_url(self, url):
        try:
            # Open the URL in the default web browser
            webbrowser.open(url)
            print(f"Opening {url} in your browser...")
        except Exception as e:
            print(f"An error occurred while trying to open the URL: {e}")


    def loadWeb(self, url):
            """Load content from a given URL."""
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

