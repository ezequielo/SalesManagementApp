__author__ = 'Nacho-w7'

from unittest import TestCase
from src.entities.base.Article import Article
from src.entities.base.Category import Category


class TestCategory(TestCase):
    """
    Test category
    Test class for testing the most interesting methods from category

    """

    def test_remove_article(self):
        """
        Test remove article
        Asserts that the article list is correctly updated after a remove operation
        """

        art1 = Article("123776789087", "Article 1", 12.0, 20.0)
        cat1 = Category(001, "CAT1", "Sample Category")
        boolean = False
        cat1.add_article(art1)
        cat1.remove_article(art1)
        for i in cat1.get_article_list():
            if i.get_ean13() == "1237767890875":
                boolean = True
        self.assertEquals(boolean, False)