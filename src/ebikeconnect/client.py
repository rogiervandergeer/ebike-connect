from requests import post


class EBikeConnectClient:
    BASE_URL = "https://www.ebike-connect.com/ebikeconnect/api"
    PAGE_SIZE = 50

    def __init__(self, cookie: str):
        self.cookie = cookie

    @classmethod
    def login(cls, username: str, password: str) -> "EBikeConnectClient":
        response = post(
            cls.BASE_URL + "/portal/login/public",
            json=dict(username=username, password=password, rememberme=True),
        )
        response.raise_for_status()
        return cls(response.cookies["REMEMBER"])
