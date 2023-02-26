import datetime

DATE_TODAY = datetime.datetime.now().strftime("%d/%m/%Y")
DATE_FORWARD_6_MONTHS = (datetime.datetime.now() + datetime.timedelta(days=(30 * 6))).strftime("%d/%m/%Y")


class FlightData:
    def __init__(self, destination_airport_code, destination_city, date_from=DATE_TODAY, date_to=DATE_FORWARD_6_MONTHS,
                 price=0):
        self.price = price
        self.departure_airport_code = "LON"
        self.departure_city = "London"
        self.destination_airport_code = destination_airport_code
        self.destination_city = destination_city
        self.date_from = date_from
        self.date_to = date_to
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 21
        self.max_stopovers = 0
        self.curr = "GBP"


class FlightDataReturn:
    def __init__(self, price, out_date, return_date, destination_airport_code, destination_city,
                 origin_airport_code, origin_city="London"):
        self.price = price
        self.destination_airport_code = destination_airport_code
        self.destination_city = destination_city
        self.origin_airport_code = origin_airport_code
        self.origin_city = origin_city
        self.out_date = out_date
        self.return_date = return_date

    def __str__(self):
        return f"{self.destination_city}: £{self.price}"
