import requests
import json

config = json.load(open('../config.json'))

def getPrayerTimes(city):
    URL = 'https://api.collectapi.com/pray/all?data.city={0}'.format(city)
    r = requests.get(url = URL, headers = {'content-type': 'application/json', 'authorization': config["COLLECT_API_KEY"]})
    response = r.json()
    return response['result'][0], response['result'][4]