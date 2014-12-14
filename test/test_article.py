__author__ = 'ezequiel'

from unittest import TestCase
from src.entities.base.Article import Article


class TestArticle(TestCase):
    """
    Test article
    Testing class for Article class methods
    """

    def test_set_ean13(self):
        """
        Test set EAN 13
        When an article is created, its init method uses set_ean(code) function in order to create a
        EAN 13 code from the 12 digit code given as a parameter
        """

        code = "124634568321"
        ean13_code = "1246345683211"

        article = Article(code, "test_article", 1, 2)
        self.assertEqual(article.get_ean13(), ean13_code)

    def test_check_ean13(self):
        """
        Test check EAN 13
        Given a 12 digit code, check_ean will return the control digit. This method aims to assert
        that control digit is correctly generated

        """

        code = "124634568321"
        self.assertEqual(Article.check_ean13(code), 1)