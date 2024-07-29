import json
import sys


def realque(basic: str, index: str, assets_path="../assets"):
    with open(f"{assets_path}/index/que.json", mode="r", encoding="utf-8") as f:
        info: list[dict] = json.loads(f.read())

    for b in info:
        if b["basic"] != basic or (not index in b["indexes"]):
            return False

    return True


def petrealque(basic: str, index: str, assets_path="../assets"):
    if not realque(basic=basic, index=index, assets_path=assets_path):
        print(f"Error! {basic} / {index} Not In Ques!")
        sys.exit(2)
