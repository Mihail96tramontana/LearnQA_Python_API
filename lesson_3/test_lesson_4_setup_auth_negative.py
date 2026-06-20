import requests
import pytest

class TestAuthorizationWithSetup:
    exclude_params = [ #параметризованные переменные выносятся в самый вверх, даже выше setup
        ('no_cookies'),
        ('no_token')
    ]

    #функция Pytest setup позволяющая вынести в неё повторяющийся код, выполняется перед каждым тестом в классе
    def setup_method(self):
        self.data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        #1-ый запрос к серверу на авторизацию
        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=self.data)  # логинимся
        assert 'auth_sid' in response1.cookies, 'Нужная Cookie не пришла от сервера'  # проверяем, что нужная кука пришла
        assert 'x-csrf-token' in response1.headers, 'csrf-токена нет в ответе от сервера'  # проверяем, что нужный заголовок пришёл
        assert 'user_id' in response1.json(), "В json ответе от сервера нет нужного поля 'user_id'"  # проверяем, что нужное поле json пришло

        self.cookies = response1.cookies.get('auth_sid')  # присваиваем переменной значение пришедшей куки для удобства
        self.token = response1.headers.get('x-csrf-token')  # аналогично
        self.user_id_from_auth_method = response1.json()['user_id']  # не используем при доставании поля .get(), потому что уже выше убедились, что поле присутствует и ошибки не будет

    #один позитивный тест. 2-ой запрос к серверу для проверки того, что авторизация прошла успешно. сравнивается id_user между 1-ым запросом и 2-ым запросом
    def test_user_authorization(self):

        response2 = requests.get('https://playground.learnqa.ru/api/user/auth', headers={'x-csrf-token':self.token}, cookies={'auth_sid':self.cookies})
        assert 'user_id' in response2.json(), "Во втором ответе от сервера в json нет поля 'user_id'"

        user_id_from_check_method = response2.json()['user_id']

        assert self.user_id_from_auth_method == user_id_from_check_method, "'user_id' не совпадает, работает некорректно" # сравниваем ответы по значению поля user_id с 1-го и 2-го запроса



    #два негативных теста с использованием параметризации
    @pytest.mark.parametrize('condition', exclude_params) #'condition' — как назвать параметр в функции, а exclude_params — откуда брать значения
    def test_negative_user_authorization(self, condition):

        if condition == 'no_cookies':
            response2 = requests.get('https://playground.learnqa.ru/api/user/auth', headers={'x-csrf-token':self.token})
        elif condition == 'no_token':
            response2 = requests.get('https://playground.learnqa.ru/api/user/auth', cookies={'auth_sid':self.cookies})

        assert 'user_id' in response2.json(), "В json ответе от сервера нет нужного поля 'user_id'"

        user_id_from_check_method = response2.json().get('user_id')

        assert user_id_from_check_method == 0, f'User авторизовался, несмотря на переменную {condition}' #проверка, что user не авторизован, поэтому значение равняется 0