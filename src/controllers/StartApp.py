__author__ = 'ezequiel'

from MainController import MainController
from DataLoader import DataLoader


if __name__ == "__main__":
    # load sample data
    sample_data = DataLoader.load_sampledata()
    controller = MainController(sample_data)
    controller.menu_redirect()