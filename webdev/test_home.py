from django.test import Client


def test_home_status_code(client: Client):
    answer = client.get('/')
    assert answer.status_code == 200
