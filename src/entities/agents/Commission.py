__author__ = 'ezequiel'

class Commission:

    # Constructor

    def __init__(self, com_name, perc):
        self.com_name = com_name
        self.perc = perc

    # Getters and setters

    def get_com_name(self):
        return self.com_name

    def set_com_name(self):
        return self.com_name

    def get_perc(self):
        return self.perc

    def set_perc(self, perc):
        self.perc = perc

    def __str__(self):
        return self.com_name+ " - " +str(self.perc)+"%"