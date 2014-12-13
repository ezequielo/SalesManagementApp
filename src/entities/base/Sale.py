__author__ = 'ezequiel'
from datetime import datetime
class Sale:

    # Constructor

    def __init__(self):
        self.date = self.GenerateDate()
        self.State = 'pending'
        self.lines = []

    # Getter and setters

    def get_date(self):
        return self.date

    def get_lines(self):
        return self.lines

    def set_lines(self,lines):
        self.lines = lines

    def add_line(self, line):
        self.lines.append(line)
    def remove_line(self, id_art):
        self.lines.remove(id_art)


    # Support methods

    def GenerateDate(self):
        return datetime.now()


    # Main methods

    def set_state(self, state):
        self.State = state

    def get_State(self):
        return self.State

    def getTotal(self):
        total = 0.0
        for linea in self.lines:
            total = total + linea.getSubtotal()
        return total

    def __str__(self):
        return str(self.get_date()) + " - State: "+self.State + " - Total: " + str(self.getTotal())

    def printInvoice(self):
        cad = "################################################\n"
        cad = cad+str(self.get_date()) + " - State: "+self.State
        cad = cad +"\n\n"
        for linea in self.get_lines():
            cad = cad+"+"+str(linea)+"\n"
        cad = cad+"\n"
        cad = cad+"\t\tTotal: "+str(self.getTotal())
        cad =cad +"\n"+"################################################"
        print cad
