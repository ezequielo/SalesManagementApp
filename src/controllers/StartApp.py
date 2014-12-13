__author__ = 'ezequiel'

from MainController import MainController
from DataLoader import DataLoader


# load sample data
data = DataLoader.loadSampleData()

controller = MainController(data)
controller.printMenu()
