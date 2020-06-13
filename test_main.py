from unittest.mock import patch

from main import get_temperature
import pytest


testes_validos = [
    (62, -14.235004, -51.92528, 16),
    (62.54, -14.235004, -51.92528, 16),
    (5, 15.58564, -13.85478, -15),
    (-13, 22.8523, 17.358746, -25),
]


@pytest.mark.parametrize("temp,lat,lng,expected", testes_validos)
def test_get_temperature_by_lat_lng(temp, lat, lng, expected):
    mock_get = patch("main.requests.get")
    temperature = {"currently": {"temperature": temp}}

    mock_g = mock_get.start()
    mock_g.return_value.json.return_value = temperature

    resp = get_temperature(lat,lng)

    mock_get.stop()

    assert resp == expected

