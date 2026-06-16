import requests

response = requests.get('https://playground.learnqa.ru/api/hello')
print(response.text)

# домашнее задание
response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)