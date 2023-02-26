# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

# Import classes
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
# Imports
import os
import datetime
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()


# Environment Variables
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')
SHEETY_GET = os.getenv('SHEETY_GET')
SHEETY_PUT = os.getenv('SHEETY_PUT')
KIWI_KEY = os.getenv('KIWI_KEY')
KIWI_QUERY = os.getenv('KIWI_QUERY_END')
KIWI_SEARCH = os.getenv('KIWI_SEARCH_END')

# Globals
LOCAL_AIRPORT = "LON"
DATE_TODAY = datetime.datetime.now().strftime("%d/%m/%Y")
DATE_FORWARD_6_MONTHS = (datetime.datetime.now() + datetime.timedelta(days=(30*6))).strftime("%d/%m/%Y")


# Initialize classes
DataManager = DataManager(SHEETY_TOKEN, SHEETY_GET, SHEETY_PUT)
FlightSearch = FlightSearch()

sheet_data = DataManager.get_location_rows()

# Update sheet data with Testing
search_objects = []
for location in sheet_data:
    if location['iataCode'] == "":
        location['iataCode'] = FlightSearch.get_IATA(location['city'], KIWI_KEY, KIWI_QUERY)
    else:
        search = FlightData(
            destination_airport_code=location['iataCode'],
            destination_city=location['city'],
            date_from=DATE_TODAY,
            date_to=DATE_FORWARD_6_MONTHS)
        result = FlightSearch.search_flight(flight_data_obj=search, key=KIWI_KEY, endpoint=KIWI_SEARCH)
        search_objects.append(result)

#pprint(sheet_data)
#DataManager.update_iata_records(sheet_data)


# FLightTest = FlightData('BA', 'Buenos Aires', DATE_TODAY, DATE_FORWARD_6_MONTHS)
# test = FlightSearch.search_flight(FLightTest, KIWI_KEY, KIWI_SEARCH)
# print(test)

for result in search_objects:
    print(result)



