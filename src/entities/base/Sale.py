__author__ = 'ezequiel'
from datetime import datetime


class Sale:
    # Constructor
    def __init__(self):
        self.date = self.generate_date()
        self.state = 'pending'
        self.lines = []

    # Getter and setters
    def get_date(self):
        return self.date

    def get_lines(self):
        return self.lines

    def set_lines(self, lines):
        self.lines = lines

    def add_line(self, line):
        self.lines.append(line)

    def remove_line(self, id_art):
        self.lines.remove(id_art)

    # Support methods
    def generate_date(self):
        return datetime.now()

    # Main methods
    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def get_total(self):
        total = 0.0
        for linea in self.lines:
            total = total + linea.get_subtotal()
        return total

    def __str__(self):
        return str(self.get_date()) + " - State: " + self.state + " - Total: " + str(self.get_total())

    def print_invoice(self):
        cad = "################################################\n"
        cad = cad + str(self.get_date()) + " - State: " + self.state
        cad += "\n\n"
        for line in self.get_lines():
            cad = cad + "+" + str(line) + "\n"
        cad += "\n"
        cad = cad + "\t\tTotal: " + str(self.get_total())
        cad = cad + "\n" + "################################################"
        print cad
