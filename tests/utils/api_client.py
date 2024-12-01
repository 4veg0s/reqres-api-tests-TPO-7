import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        return response

    def post(self, endpoint, data=None):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        return response

    def put(self, endpoint, data=None):
        response = requests.put(f"{self.base_url}/{endpoint}", json=data)
        return response

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}/{endpoint}")
        return response
