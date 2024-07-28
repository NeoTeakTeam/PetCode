import json


def listans(basic: str, index: str):
    with open(f"../assets/que/{basic}/{index}/info.json", mode="r", encoding="utf-8") as f:
        data = json.load(f)

    print("List Ans")
    print(f"Index : {basic} / {index}")
    print("------------")
    print("Ans:")
    for i in data["ans"]:
        print(f"    {i}")
