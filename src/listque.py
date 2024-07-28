import json


def showque(i: dict):
    print(f"Basic   : {i["basic"]}")

    print("Indexes :")
    for k in i["indexes"]:
        print(f"    {k}")
    print("------------")


def listque(pages: int = 1, group_size: int = 20, assets_path="../assets"):
    with open(f"{assets_path}/index/que.json", mode="r", encoding="utf-8") as f:
        info: list[dict] = json.loads(f.read())

    max_pages: int = len(info) // group_size + (1 if len(info) % 5 != 0 else 0)

    if pages > max_pages:  # 页数大于最大页数
        print("Error! Pages > Max Pages")
        exit(1)
    elif pages <= 0:  # 页数为非正数
        print("Error! Pages must > 0")
        exit(1)

    print("List Que:")
    print(f"Page: {pages} / {max_pages}")  # 显示输出页数与最大页数
    print("------------")

    group: list = info[pages * group_size -
                       group_size: pages * group_size]  # 拆分info

    for k in group:
        showque(k)
