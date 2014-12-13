__author__ = 'ezequiel'

from MainController import MainController
from DataLoader import DataLoader

# load sample data
dict = DataLoader.loadSampleData()

controller = MainController(dict)
controller.printMenu()
