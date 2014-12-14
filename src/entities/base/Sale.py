__author__ = 'ezequiel'
from datetime import datetime


class Sale:
    """

        Sale is the class of simulate a real Sale

    """
    # Constructor
    def __init__(self):
        """

        Init method for Sale with a default state and actual date generated

        """
        self.date = self.generate_date()
        self.state = 'pending'
        self.lines = []

    # Getter and setters
    def get_date(self):
        """

        Get date generated

        :return: date generated

        """
        return self.date

    def get_lines(self):
        """

        Get sale lines list

        :return: return sale lines list

        """
        return self.lines

    def set_lines(self, lines):
        """

        update exist sale line

        :param lines: new sale line list

        """
        self.lines = lines

    def add_line(self, line):
        """

        Add new sale line

        :param line: new sale line

        """
        self.lines.append(line)

    def remove_line(self, id_art):
        """

        Remove sale line

        :param id_art: article identification

        """
        self.lines.remove(id_art)

    # Support methods
    @staticmethod
    def generate_date():
        """

        Generate the actual date

        :return: actual date

        """
        return datetime.now()

    # Main methods
    def set_state(self, state):
        """

        Update exist sale state

        :param state: new sale state

        """
        self.state = state

    def get_state(self):
        """

        Get actual sale state

        :return: sale state

        """
        return self.state

    def get_total(self):
        """

        Get sale total

        :return: number total

        """
        total = 0.0
        for linea in self.lines:
            total = total + linea.get_subtotal()
        return total

    def __str__(self):
        """

        Print sale information

        :return: String instance

        """
        return str(self.get_date()) + " - State: " + self.state + " - Total: " + str(self.get_total())

    def print_invoice(self):
        """

        Print a formal sale invoice

        :return: Information necessary how String

        """
        cad = "################################################\n"
        cad = cad + str(self.get_date()) + " - State: " + self.state
        cad += "\n\n"
        for line in self.get_lines():
            cad = cad + "+" + str(line) + "\n"
        cad += "\n"
        cad = cad + "\t\tTotal: " + str(self.get_total())
        cad = cad + "\n" + "################################################"
        print(cad)
