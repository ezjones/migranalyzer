# Ez Jones 2015
# You need weatherpy and gspread for this to work
# Install them with
# sudo pip install weatherpy
# sudo pip install gspread

import weatherpy
import time
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

while True:
    locationToGrab = 12761735
    nowTime = time.strftime("%m/%d/%Y/ %H:%M:%S")
    print (nowTime)
    print ("-----------------------")
    print ("Getting Yahoo Weather...")
# Get the weather using a WOEID. 12761735 is New York
# Get yours here: http://woeid.rosselliot.co.nz/
    r = weatherpy.Response('User Agent', locationToGrab, metric=False)

    print ("-----------------------")
    print '{0}, {1} \n'.format(r.location.city, r.location.country)

    pressureHG = r.atmosphere.pressure
    pressureHPA = pressureHG * 33.8638866667
    print ("\tPressureHPA: " + str(pressureHG))
    print ("\tPressureHG: " + str (pressureHPA))

    temperature = r.condition.temperature
    humidity = r.atmosphere.humidity
    visibility = r.atmosphere.visiblity
    print ("\tTemperature: " + str (temperature))
    print ("\tHumidity: " + str(humidity))
    print ("\tVisibility" + str (visibility))

    currentCondition = r.condition.text
    forecastCondition = r.tomorrow.text
    print ("\tCurrent Condition: " + currentCondition)
    print ("\tForecast Condition: " + forecastCondition)

    temperatureHigh = r.today.high
    temperatureLow = r.today.low

    print ("\tTemperatureHigh: " + str (temperatureHigh))
    print ("\tTemperature Low: " + str (temperatureLow))

    conditionCode = r.condition.code
    forecastCode = 0 # TODO: how to get it
    print ("\tCondition Code: " + str (conditionCode))

# SEND TO GOOGLE SPREADHSHETS
    print ("Done.")
    f = open ("out.txt", "a")

    f.write("Done:" + nowTime + "\n")
    f.close()

    nextrun = 2
    print ("Waiting for next run..." + str (nextrun))
    time.sleep(nextrun)
