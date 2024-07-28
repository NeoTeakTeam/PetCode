import shutil as sl


def copyque(basic: str, index: str, output: str):
    print("Copying...", end="")
    # 复制 源文件 到 输出文件
    sl.copyfile(f"../assets/que/{basic}/{index}/temp.py", output)
    print("OK")
