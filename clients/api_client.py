import requests


class ApiClient:

    def __init__(self, base_url, token=None, timeout=5):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

        if token:
            self.session.headers.update({
                "Authorization": token
            })

    def get(self, endpoint):
        return self.session.get(
            url=f"{self.base_url}/{endpoint}",
            timeout=self.timeout
        )

    def post(self, endpoint, json=None):

        return self.session.post(
            url=f"{self.base_url}/{endpoint}",
            json=json,
            timeout=self.timeout
        )

    def put(self, endpoint, json=None):

        return self.session.put(
            url=f"{self.base_url}/{endpoint}",
            json=json,
            timeout=self.timeout
        )

    def patch(self, endpoint, json=None):

        return self.session.patch(
            url=f"{self.base_url}/{endpoint}",
            json=json,
            timeout=self.timeout
        )

    def delete(self, endpoint):

        return self.session.delete(
            url=f"{self.base_url}/{endpoint}",
            timeout=self.timeout
        )
