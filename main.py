import requests

target = input("Введите айпи: ")
url = f"http://ip-api.com/json/{target}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"IP: {target}")
    print(f"Страна: {data.get('country')}")
    print(f"Регион: {data.get('regionName')}")
    print(f"Город: {data.get('city')}")
    print(f"Провайдер: {data.get('isp')}")
    print(f"Организация: {data.get('org')}")
    print(f"Часовой пояс: {data.get('timezone')}")
    print(f"Широта: {data.get('lat')}")
    print(f"Долгота: {data.get('lon')}")

