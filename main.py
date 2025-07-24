import requests

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
        else:
            print("ошибка с api")
    else:
         print("ошибка с http")
except Exception as e:
    print(e)

