import requests
import json

# 1-ый этап. Создаём переменную со строкой json в формате str для скармливания Python
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
# 2-ой этап. Создаём ещё одну переменную и парсим: импортируем библиотеку json --> создаём переменную, в которую записываем готовый объект формата dict
data = json.loads(json_text)
# 3-ий этап. Выводим полученный результат. Конкретный поле вызываем через вложенные ключи/индексы
print(data['messages'][1]['message'])

# ещё одно задание мне для усвоения
json_t = '{"order":{"id":1234,"status":"delivered","items":[{"name":"ноутбук","price":50000},{"name":"мышка","price":1500},{"name":"клавиатура","price":3000}]}}'
data = json.loads(json_t)
print(data['order']['status'])
print(data["order"]['items'][1]['name'])
print(data['order']['items'][2]['price'])