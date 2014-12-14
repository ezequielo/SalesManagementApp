__author__ = 'ezequiel'


class Category:
    """

    Category class
    This class is responsible of modeling the category of many articles.

    """
    def __init__(self, id_cat, cat_name, desc):
        """

        Init method
        Initializes an instance of Category class given the following parameters

        :param id_cat: category identification
        :param cat_name: category name
        :param desc: description

        """
        self.cat_name = cat_name
        self.id_cat = id_cat
        self.desc = desc
        self.article_list = []
        self.commission = None
        self.org = None

    # Getter and setters

    def get_article_list(self):
        """

        Get article list
        Return an article list

        :return: article list

        """
        return self.article_list

    def set_article_list(self, article_list):
        """

        Set article list
        Allow to change the actual article list

        :param article_list: new article list

        """
        self.article_list = article_list

    def get_cat_name(self):
        """

        Get category name
        Return a category name

        :return: Category name

        """
        return self.cat_name

    def set_cat_name(self, cat_name):
        """

        Set category name
        Allow to change the actual category name

        :param cat_name: new category name

        """
        self.cat_name = cat_name

    def get_desc(self):
        """

        Get description
        Return a category description

        :return: category description

        """
        return self.desc

    def set_desc(self, desc):
        """

        Set description
        Allow to change the actual category description

        :param desc: new category description

        """
        self.desc = desc

    def get_id_cat(self):
        """

        Get id cat
        Return actual identification of category

        :return: identification category

        """
        return self.id_cat

    def set_id_cat(self, id_cat):
        """

        Get id cat
        Allow to change the actual identification of category

        :param id_cat: new category identification

        """
        self.id_cat = id_cat

    def get_commission(self):
        """

        Get commission
        Returns the actual commission of sale an product

        :return: Commission

        """
        return self.commission

    def set_commission(self, commission):
        """

        Set commission
        Allow to change the actual commission of sale an product

        :return: actual commission

        """
        self.commission = commission

    def get_org(self):
        """

        Get organization cif
        Return the organization cif

        :return: organization cif

        """
        return self.org

    def set_org(self, org):
        """

        Set organization cif
        Allow to change actual organization cif

        :param org: new organization cif

        """
        self.org = org

    # Main methods

    def is_article(self, art):
        """
        Helper method that returns True if the article is in the list or False if it is not
        :param art: Article to be checked

        """

        for article in self.article_list:
            if article.ean13 == art.ean13:
                return True
        return False

    def add_article(self, art):
        """

        Add article
        Allow to add an article to article list

        :param art: new article

        """
        if not self.is_article(art):
            self.article_list.append(art)
            return True
        else:
            return False

    def remove_article(self, art):
        """

        Remove article
        Allow to remove an article to article list

        :param art: article by this is removed

        """

        if self.is_article(art):
            self.article_list.remove(art)
            return True
        else:
            return False

    def __str__(self):
        """

        Print principal category information

        :return: Category information

        """
        return str(self.id_cat) + " - "+self.cat_name + " desc\n " + self.desc