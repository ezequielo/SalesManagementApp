__author__ = 'ezequiel'

from datetime import date
from src.entities.base.Sale import Sale

class Agent:

    # Constructor

    def __init__(self, agent_id, firstname, lastname, birthdate, base, email):
        self.agent_id = agent_id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.base = base
        self.email = email
        self.sales = []
        self.org = None

    # Getter and setters

    def get_sales(self):
        return self.sales

    def get_name(self):
        return self.lastname + ', ' +self.firstname

    def get_agent_id(self):
        return self.agent_id


    def get_edad(self):
        today = date.today()
        l=self.birthdate.split("/")
        fbir=date( int(l[2]), int(l[1]), int(l[0]))
        years = ((today.year - fbir.year - 1) +
            (1 if (today.month, today.day) >= (fbir.month, fbir.day) else 0))
        return years

    def get_birthdate(self):
        return self.birthdate

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def set_agent_id(self, new_id):
        self.agent_id=new_id

    def get_base(self):
        return self.base

    def set_base(self, base):
        self.base = base

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_org(self):
        return self.org

    def set_org(self, org):
        self.org = org


    def __str__(self):
        return self.firstname+" " + self.lastname + " - "+self.email


    # Main methods

    def getComisiones(self):
        comisiones = 0.0
        comm_perc = 0
        for sale in self.sales:
            for line in sale.lines:
                article = line.get_art()
                if article.get_commission():
                    comm_perc = article.commission.get_perc()

                else:
                    cat_list = self.org.get_categories()

                    for category in cat_list:
                            for art in category.get_list_articulos():
                                if art.get_ean13() == article.get_ean13():
                                    if category.get_commission():
                                        comision = category.get_commission()
                                        comm_perc = comision.get_perc()
                                else:
                                    comm_perc = 0.0

                comm_art = article.get_listprice() * comm_perc
                comm_line = comm_art * line.get_uds()
                comisiones = comisiones + comm_line
        return comisiones



    def getTotal(self):
        comisiones = 0.0
        comm_perc= 0.0
        for sale in self.sales:
            for line in sale.get_lines():
                article = line.get_art()
                if article.get_commission():
                    comm_perc = article.commission.get_perc()

                else:
                    cat_list = self.org.get_categories()

                    for category in cat_list:
                        for art in category.get_list_articulos():

                            if art.get_ean13() == article.get_ean13():
                                if category.get_commission():
                                    comm_perc = category.commission.get_perc()
                            else:
                                comm_perc = 0.0

            comm_art = article.get_listprice() * comm_perc
            comm_line = comm_art * line.get_uds()
            comisiones = comisiones + comm_line

        total = self.base+comisiones
        return total


    def crearVenta(self):
        v = Sale()
        self.sales.append(v)
        return v

