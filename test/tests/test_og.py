import unittest
from src.og import jokes, weather


class TestJokes(unittest.TestCase):
    def test_jokes_not_null(self):
        joke = jokes()
        self.assertIsNotNone(joke[0])
        self.assertIs(joke[1], 200)


class TestWeather(unittest.TestCase):
    def test_weather_not_null(self):
        weather_data = weather()
        self.assertIsNotNone(weather_data)
        print("test", weather_data)
        self.assertIs(weather_data['location']['name'], 'Karlstad')


if __name__ == '__main__':
    unittest.main()
