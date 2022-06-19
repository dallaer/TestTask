from googleapiclient import discovery
import httplib2
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = 'sesttask-353806-83bae27ea09e.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = discovery.build('sheets', 'v4', http = httpAuth)
spreadsheetId = '1LYFBOIXZ6Tk9rH8QI33Sev8OwTu93bfCy-1aSUbTCPg'


def append():
    range = 'Лист1!'
    print("Введите значения")
    values = [list(map(str, input().split()))]
    print("Введите ячейку")
    range += input()
    try:
        service.spreadsheets().values().append(
            spreadsheetId=spreadsheetId,
            range=range,
            valueInputOption="USER_ENTERED",
            body={'values': values}).execute()
    except :
        print("Неверный формат ввода. Введите ячейку в формате S1 и значения через пробел")
        append()


def update():
    range = 'Лист1!'
    print("Введите значения")
    values = [list(map(str, input().split()))]
    print("Введите ячейку")
    range += input()
    try:
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheetId,
            range=range,
            valueInputOption="USER_ENTERED",
            body={'values': values}).execute()
    except:
        print("Неверный формат ввода. Введите ячейку в формате S1 и значения через пробел")
        update()


def delete():
    range = 'Лист1!'
    print("Введите ячейку или диапазон")
    range += input()
    try:
        service.spreadsheets().values().clear(
            spreadsheetId=spreadsheetId,
            range=range).execute()
    except:
        print("Неверный формат ввода диапазона, Введите в формате S1 или D1:S5")
        delete()


while True:
    print("Выберите действие: append, update, delete.")
    x = input()
    if x == "append":
        append()
        print("Успешно!")
        print('Ссылка на таблицу: https://docs.google.com/spreadsheets/d/' + spreadsheetId)
        print("Для выхода из программы введите: break")
    elif x == "update":
        update()
        print("Успешно!")
        print('Ссылка на таблицу: https://docs.google.com/spreadsheets/d/' + spreadsheetId)
        print("Для выхода из программы введите: break")
    elif x == "delete":
        delete()
        print("Успешно!")
        print('Ссылка на таблицу: https://docs.google.com/spreadsheets/d/' + spreadsheetId)
        print("Для выхода из программы введите: break")
    elif x == "break":
        break
    else:
        print("Неккоректный ввод")