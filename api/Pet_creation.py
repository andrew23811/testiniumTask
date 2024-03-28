import unittest
import requests


class Create_pet(unittest.TestCase):
    def setUp(self):
        self.url = 'https://petstore.swagger.io/v2/pet'

    def test_create_pet(self):
        payload = {
            "id": 0,
            "category": {
                "id": 0,
                "name": "dogooo"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "bulldog"
                }
            ],
            "status": "available"
        }

        # Define headers
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = requests.post(self.url, json=payload, headers=headers)

        # Print the response
        print(response.status_code)
        print(response.text)

    def test_create_user(self):
        payload ={
            "id": 0,
            "username": "Andrew Albert",
            "firstName": "Andrew",
            "lastName": "Albert",
            "email": "asdd@gmail.com",
            "password": "pass",
            "phone": "012012030",
            "userStatus": 0
        }

        response = requests.post(self.url, json=payload)

        # Print the response
        print(response.status_code)
        print(response.text)


if __name__ == '__main__':
    unittest.main()


