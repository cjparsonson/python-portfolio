import requests
from flight_data import FlightData, FlightDataReturn


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    @staticmethod
    def get_iata(location: str, key: str, endpoint: str) -> str:
        # Build request
        search_header = {
            "apikey": key
        }

        search_params = {
            "term": location
        }

        response = requests.get(url=endpoint, headers=search_header, params=search_params)
        response.raise_for_status()
        location_data = response.json()
        return location_data['locations'][0]['code']

    @staticmethod
    def search_flight(flight_data_obj, key, endpoint) -> FlightDataReturn | None:
        search_header = {
            "apikey": key
        }

        search_params = {
            "fly_from": flight_data_obj.departure_airport_code,
            "fly_to": flight_data_obj.destination_airport_code,
            "date_from": flight_data_obj.date_from,
            "date_to": flight_data_obj.date_to,
            "nights_in_dst_from": flight_data_obj.nights_in_dst_from,
            "nights_in_dst_to": flight_data_obj.nights_in_dst_to,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": flight_data_obj.curr,
            "max_stopovers": 0
        }

        response = requests.get(headers=search_header, url=endpoint, params=search_params)
        response.raise_for_status()
        try:
            flight_data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {flight_data_obj.destination_city}")
            return None
        # return flight_data
        new_flight_data_obj = FlightDataReturn(
            price=flight_data['price'],
            destination_airport_code=flight_data['flyTo'],
            destination_city=flight_data['cityTo'],
            origin_airport_code=flight_data['cityCodeFrom'],
            out_date=flight_data['route'][0]['local_departure'].split("T")[0],
            return_date=flight_data['route'][1]['local_departure'].split("T")[0]
        )
        return new_flight_data_obj
