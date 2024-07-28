def showans(basic: str, index: str, ansindex: str, assets_path="../assets"):
    with open(f"{assets_path}/que/{basic}/{index}/ans/{ansindex}.py", mode="r", encoding="utf-8") as f:
        print("Ans Show")
        print("------------")
        print(f"Ans Index: {ansindex}")
        print("------------")
        print(f.read())
