from .common import *

CATTLTE_TEST_URL = os.environ.get('CATTLTE_TEST_URL','https://172.16.0.233:30443/')
ADMIN_USER = os.environ.get('ADMIN_USER','admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD','password')

HARVESTER_LOGIN_URL = '/v1-public/auth?action=login'


def test_login():
    url = CATTLTE_TEST_URL.strip('/') + HARVESTER_LOGIN_URL
    r = requests.post(url, json={
        'username': ADMIN_USER,
        'password': ADMIN_PASSWORD,
        'responseType': 'json'
    }, verify=False)

    assert r.status_code == 200