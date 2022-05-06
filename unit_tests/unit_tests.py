import abc_news
import cnn_news
import fox_news
import news_virginia_nbc
import covid_articles
import covid_numbers
import get_response

import unittest

class testingfunctions(unittest.TestCase):
    #test abc news
    def test_abc_news(self):
        actual = abc_news.abc_news()
        expected = dict
        self.assertIsInstance(actual,expected)
    #test fox news
    def test_fox_news(self):
        actual = fox_news.fox_news()
        expected = dict
        self.assertIsInstance(actual,expected)

    #test nbc news
    def test_nbc_news(self):
        actual = news_virginia_nbc.news_virginia_nbc()
        expected = dict
        self.assertIsInstance(actual, expected)
    #test cnn news
    def test_cnn_news(self):
        actual = cnn_news.cnn_news()
        expected = dict
        self.assertIsInstance(actual, expected)
    #test COVID-19 cases numbers
    def test_covid_num(self):
        actual = covid_numbers.covid_numbers(20175)
        expected = dict
        self.assertIsInstance(actual, expected)
    #test covid articles
    def test_covid_Article(self):
        actual = covid_articles.covid_articles()
        expected = dict
        self.assertIsInstance(actual, expected)

    #test get_response program with input 1
    def test_response_1(self):
        actual = get_response.get_response("cases")
        expected = "Please, enter your five digit zip code to get daily cases update: "
        self.assertEqual(actual,expected)

    #test get_response program with input 2
    def test_response_2(self):
        actual = get_response.get_response("news")
        expected = "I can provide news from \n\n 1. ABC News \n 2. FOX News \n 3. CNN News \n 4. NBC News (Exclusively for Virginia)"
        self.assertEqual(actual,expected)

    #test get_response program with input 3
    def test_response_3(self):
        actual = get_response.get_response("asdfjgldljgrpgk")
        expected = "I don't understand ! Sorry !"
        self.assertEqual(actual,expected)

