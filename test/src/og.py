import json
import requests
from main2 import *

def jokes():  # get jokes from the api
    """
    This function is used to get the jokes from the api
    and return the data
    :param f:
    :return:
    """
    link = r"https://official-joke-api.appspot.com/random_joke"  # link to the api
    data = requests.get(link, timeout=5)  # get the data from the api
    t_t = json.loads(data.text)  # load the data
    return t_t, data.status_code  # return the data


def weather():  # get weather from the api
    """
    This function is used to get the weather from the api
    :return:
    """
    access_key = "49fd86502d789706569dd23f26182bed"  # access key to the api
    query = "Karlstad"  # query to the api
    link = f"http://api.weatherstack.com/current?access_key={access_key}&query={query}"  # link to the api
    data = requests.get(link, timeout=5)  # get the data from the api
    t_t = json.loads(data.text)  # load the data
    return t_t  # return the data