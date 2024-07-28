#!python3

from fire import Fire as fire
import os

listque = __import__("listque").listque
listans = __import__("listans").listans
loadque = __import__("loadque").loadque
copyque = __import__("initque").copyque
checkque = __import__("checkque").checkque
showans = __import__("showans").showans


PetCodeAssetsPath = os.getenv("PetCodeAssetsPath") or "../assets"


class App:
    """
    Pet Code
    - A simple program for practicing coding -

    Warning!
    Que Index and Basic input info:
    q(basic) q(index)

    Answer Index input info:
    a(index)
    """

    def __init__(self) -> None:
        pass

    def listque(self):
        """
        List Que at assets/index
        """

        listque()

    def listans(self, basic: str, index: str, assets_path=PetCodeAssetsPath):
        """
        List Ans at Que

        Args:
            basic: str   # Index (Like q00)
            index: str   # Index (Like q000001)
        """

        listans(basic=basic, index=index, assets_path=assets_path)

    def loadque(self, basic: str, index: str, assets_path=PetCodeAssetsPath):
        """
        Load Que at assets/que

        Args:
            basic: str   # Index (Like q00)
            index: str   # Index (Like q000001)
        """

        loadque(basic=basic, index=index, assets_path=assets_path)

    def initque(self, basic: str, index: str, output: str, assets_path=PetCodeAssetsPath):
        """
        Init Que
        Copy Que's source file to output

        Arhs:
            basic : str    # Index (Like q00)
            index : str    # Index (Like q000001)
            output: str    # Output file (Like a.py)
        """

        copyque(basic=basic, index=index,
                output=output, assets_path=assets_path)

    def checkque(self, basic: str, index: str, ansfile: str, assets_path=PetCodeAssetsPath):
        """
        Check Que
        Real Answer?

        Args:
            basic  : str    # Index (Like q00)
            index  : str    # Index (Like q000001)
            ansfile: str    # Output file (Like a.py)
        """

        checkque(basic=basic, index=index,
                 ansfile=ansfile, assets_path=assets_path)

    def showans(self, basic: str, index: str, ansindex: str, assets_path=PetCodeAssetsPath):
        """
        Show Ans
        cat.exe Que's answer (bushi)

        Ars:
            basic   : str    # Index (Like q00)
            index   : str    # Index (Like q000001)
            ansindex: str    # Output file (Like a00)
        """

        showans(basic=basic, index=index,
                ansindex=ansindex, assets_path=assets_path)


if __name__ == "__main__":
    app = App()
    fire(app)
