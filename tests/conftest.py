# mypy: disable-error-code="return"

from os import environ

from pytest import fixture, skip

from ebikeconnect import EBikeConnectClient


@fixture(scope="function")
def client() -> EBikeConnectClient:
    return EBikeConnectClient("cookie")


@fixture(scope="session")
def authenticated_client() -> EBikeConnectClient:
    try:
        return EBikeConnectClient.login(environ["EBIKE_CONNECT_USERNAME"], environ["EBIKE_CONNECT_PASSWORD"])
    except KeyError:
        skip("Requires authentication.")
