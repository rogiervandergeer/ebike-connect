import pytest
from requests.exceptions import HTTPError

from ebikeconnect import EBikeConnectClient


class TestClient:
    def test_invalid_authentication(self):
        with pytest.raises(HTTPError) as exc:
            EBikeConnectClient.login("username", "password")
        assert exc.value.response.status_code == 403
        assert "403 Client Error" in str(exc.value)


class TestAuthenticatedClient:
    def test_cookie(self, authenticated_client: EBikeConnectClient):
        assert len(authenticated_client.cookie) > 30
