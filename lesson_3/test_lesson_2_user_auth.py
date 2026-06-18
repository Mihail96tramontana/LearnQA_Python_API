import requests
import pytest

class TestAuthorization:
    def test_user_authorization(self):
        data = {
            'email':'vinkotov@example.com',
            'password':'1234'
        }

        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)
        assert 'auth_sid' in response1.cookies, 'Нужная Cookie не пришла от сервера' #проверяем, что нужная кука пришла
        assert 'x-csrf-token' in response1.headers, 'csrf-токена нет в ответе от сервера' #проверяем, что нужный заголовок пришёл
        assert 'user_id' in response1.json(), "В json ответе от сервера нет нужного поля 'user_id'" #проверяем, что нужное поле json пришло

        cookies = response1.cookies.get('auth_sid') # присваиваем переменной значение пришедшей куки для удобства
        token = response1.headers.get('x-csrf-token') #аналогично
        user_id_from_auth_method = response1.json()['user_id'] # не используем при доставании поля .get(), потому что уже выше убедились, что поле присутствует и ошибки не будет

        response2 = requests.get('https://playground.learnqa.ru/api/user/auth', headers={'x-csrf-token':token}, cookies={'auth_sid':cookies})
        assert 'user_id' in response2.json(), "Во втором ответе от сервера в json нет поля 'user_id'"

        user_id_from_check_method = response2.json()['user_id']

        assert user_id_from_auth_method == user_id_from_check_method, "'user_id' не совпадает, работает некорректно" # сравниваем ответы по значению поля user_id с 1-го и 2-го запроса




