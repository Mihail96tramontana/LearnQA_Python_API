import requests

response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(f'1-ый запрос: {response.text}')

params_head = {'method':'HEAD'}
response = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type', params = params_head)
print(f'Текстовый ответ от метода HEAD: {response.text}')

data_post = {'method':'POST'}
response = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data=data_post)
print(f'Текстовый ответ от метода POST: {response.text}')

# вложенный цикл с запросами к API
methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']
for i in methods:
    for param in methods:
        if i == 'GET':
            response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={'method':param})
        elif i == 'POST':
            response = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': param})
        elif i == 'PUT':
            response = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': param})
        elif i == 'DELETE':
            response = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': param})
        elif i == 'HEAD':
            response = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type', params={'method': param})
        print(f'{i} + param={param}: {response.text}')
