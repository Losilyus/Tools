import sys
import module.prayersTimes as prayer
import module.prayersAll as prayers
import module.prayersRamazan as ramazan
import json

config = json.load(open('../config.json'))


if len(sys.argv) == 3:
    if sys.argv[1] == 'ramazan':
        response = ramazan.getPrayerTimes(sys.argv[2])
        print(response)
    else:
        response = prayer.getPrayerTimes(sys.argv[1], sys.argv[2])
        print(response)

elif len(sys.argv) == 2:
    if sys.argv[1] == 'ramazan':
        response = ramazan.getPrayerTimes(config['CITY'])
        print(response, 'Ramazan')
    else:
        response = prayer.getPrayerTimes(config["CITY"], sys.argv[1])
        print(response)

else:
    response = prayers.getPrayerTimes(config["CITY"])
    print(response)
