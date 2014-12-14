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
        cat1.add_article(art1)

        self.assertEqual(len(cat1.article_list), 1)
        self.assertTrue(cat1.remove_article(art1))
        self.assertEqual(len(cat1.article_list), 0)
        self.assertFalse(cat1.remove_article(art1))

    def test_add_article(self):
        """
        Test remove article
        Asserts that the article list is correctly updated after an adding operation

        """
        art1 = Article("123776789087", "Article 1", 12.0, 20.0)
        cat1 = Category(001, "CAT1", "Sample Category")

        self.assertTrue(cat1.add_article(art1))
        self.assertFalse(cat1.add_article(art1))

