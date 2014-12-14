__author__ = 'ezequiel'


class SaleLine:
    """

    Sale line class
    This class is responsible of modeling the sae lines of a given sale.

    """
    def __init__(self, uds, art):
        """

        Init method
        Initializes an instance of SaleLine class given the following parameters

        :param uds: Number of units
        :param art: Article object
        :return: An instance of SaleLine class

        """
        self.art = art
        self.uds = uds

    # Getter and setters
    def get_art(self):
        """

        Get article
        Returns an article object representing the article of the line

        :return: Article object

        """
        return self.art

    def set_art(self, article):
        """

        Set article
        Allows to set an article to a given sale line

        :param article: Article object

        """
        self.art = article

    def get_uds(self):
        """

        Get units
        Returns the number representing the sale line units

        :return: Number of units

        """
        return self.uds

    def set_uds(self, uds):
        """

        Get units
        Allows to set a new number units

        :return: Number of units

        """
        self.uds = uds

    # Main methods
    def get_subtotal(self):
        """

        Get subtotal
        This method is responsible of compute the subtotal of every line given its article and units.

        :return: Line subtotal

        """
        if self.get_art().get_promotion():
            promo = self.get_art().get_promotion()
            st = self.get_uds() * self.get_art().get_list_price() * promo.get_perc()
        else:
            st = self.get_uds() * self.get_art().get_list_price()
        return st

    def __str__(self):
        """

        String method
        Allows printing SaleLine objects in a natural way

        :return: String containing the sale line info

        """
        return str(self.art) + 'uds: ' + str(self.get_uds()) + ' subtotal: ' + str(self.get_subtotal())