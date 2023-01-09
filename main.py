import json
import pprint
import requests

BASE_URL = "https://api.stackexchange.com/"
pagenumber = 1
params = {
    "order": "desc",
    "page": 1,
    "pagesize": "100",
    "fromdate": "1673136000",
    "todate": "1673222400",
    "sort": "activity",
    "site": "stackoverflow",
    "tagged": "python",
}

z = {}
z["has_more"] = True


while z["has_more"]:    # Проверяю есть ли ещё страницы с ответами

    response = requests.get(f"{BASE_URL}/2.3/questions", params=params)
    z = response.json()
    params["page"] += 1
    if  params["page"] > 10:
        break

pprint.pprint(z)

with open("data.json", "w", encoding="utf-8") as f: #Сохраняю отвкет в файл json
    json.dump(response.json(), f, ensure_ascii=False, indent=4)


