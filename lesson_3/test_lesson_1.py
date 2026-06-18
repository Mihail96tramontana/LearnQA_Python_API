import requests
import pytest


class TestFirstAPI:
    names=[
        ('Леонид'),
        ('Mikhail'),
        ('')
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = 'https://playground.learnqa.ru/api/hello'
        data = {'name':name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, 'Некорректный код ответа сервера'

        response_dict = response.json()
        assert 'answer' in response_dict, "Поле 'answer' не найдено в ответе от сервера"

        if len(name) == 0:
            expected = "Hello, someone"
        else:
            expected = f"Hello, {name}"
        assert response_dict['answer'] == expected, "Значение в поле 'answer' приходит некорректное"


