import json
import io
import sys


def checkque(basic: str, index: str, ansfile: str):
    print("Check Que")
    print(f"Index      : {basic} / {index}")
    print(f"Input File : {ansfile}")
    print("------------")
    print("Log :")
    print("Init Function...", end="")

    sin, sout = [], []  # 处理函数输入 预期输出
    check_func = ""    # 处理函数名称

    with open(f"../assets/que/{basic}/{index}/info.json", mode="r", encoding="utf-8") as f:
        info: dict = json.loads(f.read())
        for i in info["check"]:  # 加载check的列表
            sin.append(i[0])    # 添加函数输入
            sout.append(i[1])   # 添加函数输出

        check_func = info["check_func"]  # 添加函数名称

    lower_mode: bool = info["lower_mode"]

    result: bool = False  # 定义 result

    func_in, func_out = "", ""  # 定义第一次执行的函数输入 预期输出

    for k, v in zip(sin, sout):  # 遍历所有输入 预期输出
        for ik in k:   # 由于k还是个list, 因此继续遍历
            if ik == "Noarg":  # 如果ik是Noarg, 那么就是不用输入参数
                continue  # 继续下一个, 防止大聪明

            func_in += ik + ", "  # 添加单次函数输入 用, 是为了处理更多参数
        func_out = v  # 处理预期输出

    print("OK")
    print("Check file...", end="")

    with open(ansfile, mode="r", encoding="utf-8") as f:
        func_io = io.StringIO()  # 创建新io 为了处理输出
        sys.stdout = func_io  # 切换io
        exec(f"{f.read()}\n{check_func}({func_in})")  # 执行函数
        sys.stdout = sys.__stdout__  # 切换原来的io

        res_left = ""
        res_right = ""

        if lower_mode:
            res_left = str(func_io.getvalue()).strip().lower()
            res_right = func_out.lower()

        else:
            res_left = str(func_io.getvalue()).strip()
            res_right = func_out

        result = res_left == res_right   # 处理输出是否是预期输出

    print("OK")
    print("------------")
    print("Result :")

    if result:
        print("Pass")
    else:
        print("Fail")
        print("------------")
        print("Error on :")
        print(f"    Input     : {func_in}")
        print(f"    Want Out  : {func_out}")
        print(f"    Real Out  : {str(func_io.getvalue()).strip()}")