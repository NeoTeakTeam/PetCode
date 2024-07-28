import json


def realans(basic: str, index: str, ansindex: str, assets_path="../assets"):
    with open(f"{assets_path}/que/{basic}/{index}/info.json", mode="r", encoding="utf-8") as f:
        data = json.load(f)

    if ansindex in data["ans"]:
        return True

    return False


def petrealans(basic: str, index: str, ansindex: str, assets_path="../assets"):
    if not realans(basic=basic, index=index, ansindex=ansindex, assets_path=assets_path):
        print("Error! Ans Index Not In Anses!")
        exit(2)
