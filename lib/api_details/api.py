import json

base_url = "https://restful-booker.herokuapp.com/"
headers = {'content-type': 'application/json'}

# Docstrings to be added for the whole class


class APIRequest:

    @staticmethod
    def create_booking(request_session, body):
        response = request_session.post(base_url+"booking", data=json.dumps(body), headers=headers)
        return response

    @staticmethod
    def get_booking(request_session, booking_id):
        response = request_session.get(base_url+"booking/"+str(booking_id))
        return response

    @staticmethod
    def update_booking(request_session, body, booking_id, token):
        headers.update({'Cookie': "token="+token})
        response = request_session.put(base_url+"booking/"+str(booking_id), data=json.dumps(body), headers=headers)
        return response

    @staticmethod
    def generate_auth_token(request_session):
        body = {
        "username" : "admin",
        "password" : "password123"
        }
        response = request_session.post(base_url + "auth", data=json.dumps(body), headers=headers)
        return response.json()

    @staticmethod
    def delete_booking(request_session, booking_id, token):
        headers.update({'Cookie': "token=" + token})
        response = request_session.delete(base_url+"booking/"+str(booking_id),  headers=headers)
        return response

    @staticmethod
    def get_booking_ids(request_session):
        response = request_session.get(base_url + "booking")
        return response.json()

