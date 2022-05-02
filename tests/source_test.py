import unittest
from app.models import News_Source

class News_SourceTest(unittest.TestCase):
    def setUp(self):
        self.news_source = News_Source(1234,'Test_Source','Test_Description','Test_Url')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.news_source,News_Source))