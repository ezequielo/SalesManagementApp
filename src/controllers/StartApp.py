__author__ = 'ezequiel'

from MainController import MainController
from DataLoader import DataLoader


if __name__ == "__main__":
    # load sample data
    dict = DataLoader.loadSampleData()

    controller = MainController(dict)
    controller.menu_redirect()