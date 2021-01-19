import requests

def client():
    # Registration

    # data = {
    #     "username": "resttest2",
    #     "email": "test2@rest.com",
    #     "password1": "changeme123",
    #     "password2": "changeme123"
    # }

    # response = requests.post("http://localhost:8000/api/rest-auth/registration/",
    #                             data=data)

    # Authentication with Token

    token_h = "Token 3cd2bca49959be1c3fdbeceb8fd769eeef48ccff"
    headers = {"Authorization": token_h}

    response = requests.get("http://localhost:8000/api/profiles/",
                            headers=headers)

    print("Status code:", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()