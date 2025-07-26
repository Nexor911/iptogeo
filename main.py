import requests
import webbrowser

target = input("Введите айпи: ").strip()

if not target:
    print("Введен неверный ip адрес")
    input()
    exit()

url = f"http://ip-api.com/json/{target}"

try:
    response = requests.get(url)
    if response.status_code == 200:
        itog = response.json()
        if itog["status"] == "success":
            print(f"IP: {target}")
            print(f"Страна: {itog.get('country')}")
            print(f"Регион: {itog.get('regionName')}")
            print(f"Город: {itog.get('city')}")
            print(f"Провайдер: {itog.get('isp')}")
            print(f"Организация: {itog.get('org')}")
            print(f"Часовой пояс: {itog.get('timezone')}")
            print(f"Широта: {itog.get('lat')}")
            print(f"Долгота: {itog.get('lon')}")

            geo = input("Открыть результат в браузере? (y/n): ")
            if geo == "y":
                webbrowser.open(f"https://www.google.com/maps/search/?q={itog.get('lat')} {itog.get('lon')}")
        else:
            print(f"api вернул ошибку: {itog.get('message')}")
    else:
         print(f"ошибка http: status {response.status_code}")
except Exception as e:
    print(e)
