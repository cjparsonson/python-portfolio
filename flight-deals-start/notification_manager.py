from flight_data import FlightDataReturn
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, result_object: FlightDataReturn, sid, auth, to_number, from_number):
        self.result_object = result_object
        self.SID = sid
        self.Auth = auth
        self.to_number = to_number
        self.from_number = from_number
        self.client = Client(self.SID, self.Auth)

        self.notification_body = f"""
        Low Price Alert.
        From: {result_object.origin_city} {result_object.origin_airport_code}
        To: {result_object.destination_city} {result_object.destination_airport_code}
        Dates: {result_object.out_date} to {result_object.return_date}
        Price: £{result_object.price}
        """

        self.message = self.client.messages \
            .create(
                body=self.notification_body,
                from_=self.from_number,
                to=to_number
            )
        print(self.message.sid)
