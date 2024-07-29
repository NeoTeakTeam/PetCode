# Pet Code 使用文档

安装 _(编译)_ 全教程

## 安装前准备

-   需安装 Python3.12 及以上版本
-   需安装一些库文件
    ```pwsh
    pip install -U -r target/Python/needlibs.txt
    ```
-   需要设备支持 make

## 编译

Windows 平台:

```pwsh
cd target/build

# debug 编译
make TARGET=Windows VERSION=debug build

# release 编译
make TARGET=Windows VERSION=release build
```

Linux 平台:

```bash
cd target/build

# debug 编译
make TARGET=Linux VERSION=debug build

# release 编译
make TARGET=Linux VERSION=release build
```

## 环境变量设置

| 名称              | 值                             |
| ----------------- | ------------------------------ |
| PetCodeAssetsPath | 你的 assets 文件夹的路径       |
| Path              | 添加编译后的文件(如果你需要)夹 |
