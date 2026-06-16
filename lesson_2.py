import requests


payload = {'name':'Mihail'}
response = requests.get('https://playground.learnqa.ru/api/hello', params=payload)
print(response.text)
print()

# парсинг json ответа и вывод ключа
payload = {'name':'User'} # записываем в переменную параметр запроса
response = requests.get('https://playground.learnqa.ru/api/hello', params=payload) # отправляем запрос на сервер
print(response.json()['answer']) # парсим json ответ и достаём его по ключу answer
print()

# отрпавка post запроса
response = requests.post('https://playground.learnqa.ru/api/check_type', data={'key1':'value1'})
print(response.text)
print()

response = requests.get('https://playground.learnqa.ru/api/get_500', data={'key1':'value1'})
print(response.status_code)
print(response.text) # ничего не вернёт, потому что текста никакого нет на эндпоинте, только код ответа
print()

response = requests.post('https://playground.learnqa.ru/api/get_301', allow_redirects=True)
print(response.status_code)
print()

response = requests.post('https://playground.learnqa.ru/api/get_301', allow_redirects=True)
first_url = response.history[0] # записываем в переменную первый url, на который попадаем
print(response.history) # выводим промежуточную историю
print(response.status_code) # выводим финальный статус код
print(first_url.url) # выводим первый url, на который попадаем
print(response.url) # выводим финальный url
print()

payload = {'some_header':'123'}
response = requests.get('https://playground.learnqa.ru/api/show_all_headers', headers=payload)
print(response.text) # выводит заголовки отправленные в запросе
print(response.headers) # выводит заголовки отправленные в ответе сервером обратно
print()

payload = {'login':'secret_login','password':'secret_pass'}
response1 = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)
print(response.text)
print(response.status_code)
print(dict(response.cookies))
print(response.headers)
print()

# отправляем 1-ый запрос с кредами (креды в теле запроса - form-data, метод POST) на сервис (для авторизации)
payload = {'login':'secret_login','password':'secret_pass8'}
response_cookies = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)
# проверяем, что кука пришла
if response_cookies.cookies.get('auth_cookie') is not None:
    response = requests.post('https://playground.learnqa.ru/api/check_auth_cookie', cookies=response_cookies.cookies) # 2-ой запрос. После авторизации проверяем, что cookie действительны и мы авторизованы
    print(response.text)
else:
    print('Cookie не пришло, авторизация не удалась!')





