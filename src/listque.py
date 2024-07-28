import json


def listque():
    with open("../assets/index/que.json", mode="r", encoding="utf-8") as f:
        info: list[dict] = json.loads(f.read())
        print("List Que:")
        print("------------")
        for i in info:
            print(f"Index  : {i["basic"]} / {i["index"]}")
            print(f"Name   : {i["name"]}")
            print(f"Author : {i["author"]}")
            print(f"Info   : {i["info"]}")
            print("------------")
