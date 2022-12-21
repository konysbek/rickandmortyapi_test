import requests
import pytest

# проверить на 404

# BASE_LINK - основная ссылка, по которой будем тестировать API сайте Rick and Morty
BASE_LINK = "https://rickandmortyapi.com/api/"
BAD_LINK = "https://rickandmortyapi.com/apii/"

@pytest.mark.parametrize('link', ['character', 'location', 'episode'])
def test_is_200(link):
    res = requests.get(BASE_LINK + link)
    assert res.status_code == 200

# добавил тест на несуществующий линк, мало ли
# нужно придумать другие пути для тестирования
def test_is_400():
    bad_res = requests.get(BAD_LINK)
    assert bad_res.status_code == 404

@pytest.mark.parametrize('link', ['character', 'location', 'episode'])
def test_base_api(link):
    res = requests.get(BASE_LINK)
    assert res.status_code == 200
    assert BASE_LINK + link in res.json().values()

# тест на рандомные значения в ссылке
# должно выдавать 404
@pytest.mark.parametrize('sym', ['abc', 'def', '0824365t978rgcynildsy', '!@#$%^&*()_', 'we want to be better'])
def test_random_char_set(sym):
    random_res = requests.get(BASE_LINK + sym)
    assert random_res.status_code == 404

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



# болванки для тестов выбора персонажа, эпизода,
# выбора персонажа в эпизоде
def test_character_selection():
    pass


def test_episode_selection():
    pass


def test_char_ep_selection():
    pass

