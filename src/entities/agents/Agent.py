__author__ = 'ezequiel'

from datetime import date
from src.entities.base.Sale import Sale


class Agent:
    # Constructor
    def __init__(self, agent_id, first_name, last_name, birth_date, base, email):
        self.agent_id = agent_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.base = base
        self.email = email
        self.sales = []
        self.org = None

    # Getter and setters
    def get_sales(self):
        return self.sales

    def get_name(self):
        return self.last_name + ', ' + self.first_name

    def get_agent_id(self):
        return self.agent_id

    def get_age(self):
        today = date.today()
        l = self.birth_date.split("/")
        f_bir = date(int(l[2]), int(l[1]), int(l[0]))
        years = ((today.year - f_bir.year - 1) +
                (1 if (today.month, today.day) >= (f_bir.month, f_bir.day) else 0))
        return years

    def get_birth_date(self):
        return self.birth_date

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

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
        return self.first_name + " " + self.last_name + " - " + self.email

    # Main methods
    def get_commissions(self):
        commissions = 0.0
        comm_percentage = 0
        for sale in self.sales:
            for line in sale.lines:
                article = line.get_art()
                if article.get_commission():
                    comm_percentage = article.commission.get_perc()
                else:
                    cat_list = self.org.get_categories()
                    for category in cat_list:
                            for art in category.get_list_articulos():
                                if art.get_ean13() == article.get_ean13():
                                    if category.get_commission():
                                        commissions = category.get_commission()
                                        comm_percentage = commissions.get_perc()
                                else:
                                    comm_percentage = 0.0
                comm_art = article.get_listprice() * comm_percentage
                comm_line = comm_art * line.get_uds()
                commissions = commissions + comm_line
        return commissions

    def get_total(self):
        commissions = 0.0
        comm_percentage = 0.0
        article = None
        line = None
        for sale in self.sales:
            for line in sale.get_lines():
                article = line.get_art()
                if article.get_commission():
                    comm_percentage = article.commission.get_percentage()
                else:
                    cat_list = self.org.get_categories()
                    for category in cat_list:
                        for art in category.get_article_list():
                            if art.get_ean13() == article.get_ean13():
                                if category.get_commission():
                                    comm_percentage = category.commission.get_percentage()
                            else:
                                comm_percentage = 0.0
            comm_art = article.get_list_price() * comm_percentage
            comm_line = comm_art * line.get_uds()
            commissions = commissions + comm_line
        total = self.base + commissions
        return total

    def create_sale(self):
        v = Sale()
        self.sales.append(v)
        return v