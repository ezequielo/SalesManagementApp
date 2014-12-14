from src.entities.base.Article import Article
from unittest import TestCase
from src.entities.promotions.Promotion import Promotion

__author__ = 'ezequiel'


class TestPromotion(TestCase):
    """
    Test class for testing Promotion methods

    """

    def test_remove_article(self):
        """
        Asserts that the article list is correctly updated after a remove operation

        """

        art1 = Article("123776789087", "Article 1", 12.0, 20.0)
        art2 = Article("123543654321", "Article 2", 2.0, 3.0)

        promotion = Promotion("Sample promotion", 10, 0)

        promotion.add_article(art1)

        self.assertTrue(promotion.remove_article(art1))
        self.assertFalse(promotion.remove_article(art2))

    def test_add_article(self):
        """
        Asserts that the article list is correctly updated after an adding operation

        """

        art1 = Article("123776789087", "Article 1", 12.0, 20.0)
        promotion = Promotion("Sample promotion", 10, 0)

        self.assertTrue(promotion.add_article(art1))
        self.assertEqual(len(promotion.article_list), 1)


