from lib.api_details.api import APIRequest
import pytest
import random
from utilities.parse_csv import get_test_data

class TestAPI:

    @pytest.fixture(autouse=True)
    def get_requests_session(self, requests_session, logger):
        self.request_session, self.auth_token = requests_session
        self.logger = logger


    def get_random_booking_id(self):
        all_bookings = APIRequest.get_booking_ids(self.request_session)
        random_id = random.choice(all_bookings)
        return random_id['bookingid']

    @pytest.mark.parametrize(("firstname", "lastname", "totalprice" , "depositpaid",
                             "checkin", "checkout", "additionalneeds", "result"), get_test_data())
    def test_create_booking(self, firstname, lastname, totalprice, depositpaid, checkin, checkout,
                            additionalneeds, result):
        """ ***** Testcase to verify create booking API *****"""
        self.logger.info("***** Testcase to verify create booking API *****")
        booking_details = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }
        response = APIRequest.create_booking(self.request_session, booking_details)
        assert (response.status_code == 200) == result, "Create booking result is as expected"
        self.logger.info(f"Status code of create booking response is {response.status_code}")
        try:
            output = response.json()
            self.logger.info(f"Booking successful with id {output['bookingid']}")
        except ValueError:
            self.logger.info(f"Booking not successful")

    def test_get_booking(self):
        """ ***** Testcase to verify get booking API *****"""
        self.logger.info("***** Testcase to verify get booking API *****")
        booking_id = self.get_random_booking_id()
        response = APIRequest.get_booking(self.request_session, booking_id)
        self.logger.info(f"Status code of get booking API response is {response.status_code}")
        assert response.status_code == 200, "Getting booking not successful"
        try:
            output = response.json()
            self.logger.info(f"Booking details obtained for booking id:{id}")
            self.logger.info("Customer details:")
            self.logger.info(f"Name: {output['firstname']}")
            self.logger.info(f"Checkin date: {output['bookingdates']['checkin']}")
        except ValueError:
            self.logger.info(f"Getting booking details failed for booking id {id}")


    @pytest.mark.parametrize(("firstname", "lastname", "totalprice" , "depositpaid",
                             "checkin", "checkout", "additionalneeds", "result"), get_test_data())
    def test_update_booking(self, firstname, lastname, totalprice, depositpaid, checkin, checkout,
                            additionalneeds, result):
        """ ***** Testcase to verify create booking API *****"""
        self.logger.info("***** Testcase to verify update booking API *****")
        booking_details = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }
        booking_id = self.get_random_booking_id()
        response = APIRequest.update_booking(self.request_session, booking_details, booking_id, self.auth_token)
        assert (response.status_code == 200) == result, "Create booking result is as expected"
        self.logger.info(f"Status code of update API response is {response.status_code}")
        try:
            response.json()
            self.logger.info(f"Update successful for booking id {booking_id}")
        except ValueError:
            self.logger.info(f"Update not successful for booking id {booking_id}")

    def test_delete_booking(self):
        """ ***** Testcase to verify delete booking API *****"""
        self.logger.info("***** Testcase to verify delete booking API *****")
        booking_id = self.get_random_booking_id()
        response = APIRequest.delete_booking(self.request_session, booking_id, self.auth_token)
        self.logger.info(f"Status code of delete API response is {response.status_code}")
        assert response.status_code == 201, "Deleting booking not successful"

