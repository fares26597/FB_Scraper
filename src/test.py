import unittest
import scraper

#testing attempt
class TestScraper(unittest.TestCase):

    def test_posts(self):
        data = scraper.scraper("Marvel", 1)
        assert data is not None