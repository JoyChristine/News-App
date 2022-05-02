import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    # author, title, description, url, image, publishedDate
    def setUp(self):
        self.news_headlines = Article(
        'Richard Fausset',
        'Georgia Jury to Consider Whether Trump Illegally Interfered in 2020 Election - The New York Times',
        'The panel will have up to a year to recommend whether the prosecutor should pursue criminal charges against the former president and his allies.',
        'https://www.nytimes.com/2022/05/02/us/trump-election-georgia-grand-jury.html'
        'https://static01.nyt.com/images/2020/05/02/us/politics/02georgia-jury-trump-election/02georgia-jury-trump-election-thumbStandard.jpg',
        '2020-05-02T17:00:00Z')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.news_source,Article))