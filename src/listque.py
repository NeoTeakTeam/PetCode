import json


def showque(i: dict):
    print(f"Index  : {i["basic"]} / {i["index"]}")
    print(f"Name   : {i["name"]}")
    print(f"Author : {i["author"]}")
    print(f"Info   : {i["info"]}")
    print("------------")


def listque(pages: int = 0, group_size: int = 5, assets_path="../assets"):
    with open(f"{assets_path}/index/que.json", mode="r", encoding="utf-8") as f:
        info: list[dict] = json.loads(f.read())

    max_pages: int = len(info) // group_size + (1 if len(info) % 5 != 0 else 0)

    print("List Que:")
    print(f"Page: {pages}")
    print("------------")

    group: list = info[pages * group_size - 5: pages * group_size]

    for k in group:
        showque(k)
