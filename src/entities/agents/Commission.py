__author__ = 'ezequiel'


class Commission:
    """

    Commission class
    Responsible of modeling the commission objects

    """
    def __init__(self, com_name, percentage):
        """

        Init method
        Initializes and returns an instance of Commission

        :param com_name: Commission name
        :param percentage: Commission percentage
        :return: An instance of Commission

        """
        self.com_name = com_name
        self.percentage = percentage

    # Getters and setters
    def get_com_name(self):
        """

        Get commission name
        Returns the commission name of the commission objects that calls the method

        :return: Commission name

        """
        return self.com_name

    def set_com_name(self):
        return self.com_name

    def get_percentage(self):
        """

        Get percentage
        Returns the commission percentage of the commission objects that calls the method

        :return: Commission percentage

        """
        return self.percentage

    def set_percentage(self, percentage):
        """

        Set percentage
        Allows to reset the commission percentage to a new value

        :param percentage: Value representing the new percentage

        """
        self.percentage = percentage

    def __str__(self):
        """

        String method
        Allows to print Commission objects in a more natural way

        :return: String containing commission's info

        """
        return self.com_name + " - " + str(self.percentage) + "%"