__author__ = 'ezequiel'


class Commission:
    # Constructor
    def __init__(self, com_name, percentage):
        self.com_name = com_name
        self.percentage = percentage

    # Getters and setters
    def get_com_name(self):
        return self.com_name

    def set_com_name(self):
        return self.com_name

    def get_percentage(self):
        return self.percentage

    def set_percentage(self, percentage):
        self.percentage = percentage

    def __str__(self):
        return self.com_name + " - " + str(self.percentage) + "%"