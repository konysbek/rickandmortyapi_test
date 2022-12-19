import requests
import pytest

# BASE_LINK - основная ссылка, по которой будем тестировать API сайте Rick and Morty
BASE_LINK = "https://rickandmortyapi.com/api/"


@pytest.mark.parametrize('link', ['character', 'location', 'episode'])
def test_is_200(link):
    res = requests.get(BASE_LINK + link)
    assert res.status_code == 200


@pytest.mark.parametrize('link', ['character', 'location', 'episode'])
def test_base_api(link):
    res = requests.get(BASE_LINK)
    assert res.status_code == 200
    assert BASE_LINK + link in res.json().values()


def test_character_api():
    char_res = requests.get(BASE_LINK + "character")
    assert char_res.status_code == 200
    assert char_res.json()['info']['count'] == 826
    assert char_res.json()['info']['pages'] == 42
    assert char_res.json()['info']['next'] == BASE_LINK + "character?page=2"


def test_locations_api():
    loc_res = requests.get(BASE_LINK + "location")
    assert loc_res.status_code == 200


def test_episodes_api():
    ep_res = requests.get(BASE_LINK + "episode")
    assert ep_res.status_code == 200