import pytest
from fastapi.testclient import TestClient

from my_poke_api.main import app


client = TestClient(app)


@pytest.mark.parametrize(
    "region, first, last",
    [
        ["kanto", "bulbasaur", "mew"],
        ["johto", "chikorita", "celebi"],
        ["hoenn", "treecko", "deoxys-normal"],
        ["sinnoh", "turtwig", "giratina-altered"],
        ["unova", "victini", "genesect"],
        ["kalos", "chespin", "mewtwo"],
        ["alola", "rowlet", "marshadow"],
        ["galar", "grookey", "eternatus"],
        ["paldea", "sprigatito", "miraidon"],
    ],
)
def test_main_valid_region(region: str, first: str, last: str):
    with TestClient(app) as client:
        response = client.get(f"/{region}")
        data = response.json()

        assert response.status_code == 200
        assert data[0]["name"] == first
        assert data[-1]["name"] == last


def test_invalid_region():
    with pytest.raises(KeyError):
        client.get("/invalid-region")
