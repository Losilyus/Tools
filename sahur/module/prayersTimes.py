import requests
import json

config = json.load(open('../config.json'))

def getPrayerTimes(city, time):
    URL = 'https://api.collectapi.com/pray/single?ezan={1}&data.city={0}'.format(city, time)
    r = requests.get(url = URL, headers = {'content-type': 'application/json', 'authorization': config["COLLECT_API_KEY"]})
    response = r.json()
    return response