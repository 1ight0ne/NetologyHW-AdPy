import requests

from conf import YA_TOKEN

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'OAuth {YA_TOKEN}'
}


def create_folder(path):
    response = requests.put(f'{URL}?path={path}', headers=headers)
    return response.status_code


def delete_folder(path):
    response = requests.delete(f'{URL}?path={path}&permanently=true',
                               headers=headers)
    return response.status_code


def get_folder(path):
    response = requests.get(f'{URL}?path={path}', headers=headers)
    return response.status_code


class TestSomething:

    def setup(self):
        delete_folder('test')

    def teardown(self):
        delete_folder('test')

    def test_create_folder_409(self):
        create_folder('test')
        assert create_folder('test') == 409

    def test_create_folder_201(self):
        assert create_folder('test') == 201

    def test_get_folder_200(args):
        create_folder('test')
        assert get_folder('test') == 200

    def test_get_folder_404(args):
        assert get_folder('test') == 404
