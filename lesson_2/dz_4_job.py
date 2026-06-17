import requests
import time


response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job') #при запросе создаётся задача
print(response.text) #возвращаем от сервера json ответ
token = response.json()['token'] #записываем в переменную значение токена
seconds = response.json()['seconds'] #записываем в переменную кол-во секунд необходимых для выполнения джобы

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={'token':token}) #делаем запрос с полученным токеном из предыдущего запроса
print(response.text) # выводим ответ сервера со статусом работы джобы
if response.json()['status'] == "Job is NOT ready": # удостоверяемся, что джоба работу не завершила
    print(f'Ожидаемый статус: джоба не завершила работу. Нужно подождать: {seconds} секунд')
else:
    print('Не ожидаемый статус:джоба завершила работу раньше времени. Ошибка.')

time.sleep(seconds) #ожидаем ровно столько секунд сколько необходимо для завершения задачи

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={'token':token}) #делаем запрос с полученным токеном снова
print(response.text)
if response.json()['status'] == "Job is ready" and 'result' in response.json():
    print('Работа джобы выполнена успешно')
else:
    print('Что-то пошло не так!')


