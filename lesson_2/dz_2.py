import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
print(f'История промежуточных редиректов: {response.history}')
print(f'Финальный url после всех редиректов:{response.url}')