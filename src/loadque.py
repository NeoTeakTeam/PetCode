import json


def loadque(basic: str, index: str):
    with open(f"../assets/que/{basic}/{index}/info.json", mode="r", encoding="utf-8") as f:
        info: dict = json.loads(f.read())
        print("Que Info:")
        print("------------")
        print(f"Name   : {info["name"]}")
        print(f"Author : {info["author"]}")
        print(f"Info   : {info["info"]}")
        print("------------")
        print("Desc :")
        for i in info["desc"]:
            print(i)
        print("------------")
