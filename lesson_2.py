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
first_url = response.history[0]
print(response.history)
print(response.status_code)
print(first_url.url)
print(response.url)


