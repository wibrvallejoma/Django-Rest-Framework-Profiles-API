import requests

def client():
    token_h = "Token a65498881fb48d474190445aea1ca602ef8b45a6"
    # credentials = {
    #     "username": "admin",
    #     "password": "123"
    # }

    # response = requests.post("http://localhost:8000/api/rest-auth/login/",
    #                             data=credentials)

    headers = {"Authorization": token_h}

    response = requests.get("http://localhost:8000/api/profiles/",
                            headers=headers)

    print("Status code:", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()