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
    print ("\tCondition Code: " + str (conditionCode))

# SEND TO GOOGLE SPREADHSHETS
    print ("Sending to Google SpreadSheets...")

#  You need to create the OAuth2 keys for authentication
# Check the gspread documentation
# https://developers.google.com/identity/protocols/OAuth2
# Put them in the file migrakeys.json
# I read it from a file outside the repo
    json_key = json.load(open('../migrakeys.json'))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

    gc = gspread.authorize(credentials)

#  Name of your Google SpreadSheet
#  Remember to share the Spreadsheet with the long email that Google OAuth2 gave you.
# It wont work if you dont share it
    mySpreadsheet = gc.open ("Migranalyzer_Ez")
    worksheet = mySpreadsheet.get_worksheet(0)

    worksheet.append_row ([nowTime, pressureHPA, pressureHG, temperature, humidity, visibility, currentCondition, forecastCondition, temperatureHigh, temperatureLow, conditionCode], locationToGrab, r.location.city, r.location.country)

    print ("Done.")
    nextrun = 1800
    print ("Waiting for next run..." + str (nextrun))
    time.sleep(nextrun)
