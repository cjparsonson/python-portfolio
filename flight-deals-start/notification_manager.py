from flight_data import FlightDataReturn


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, result_object: FlightDataReturn, sid, auth):
        self.result_object = result_object
        self.SID = sid
        self.Auth = auth

