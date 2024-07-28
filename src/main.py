#!python3

from fire import Fire as fire
import os

listque = __import__("listque").listque
listans = __import__("listans").listans
loadque = __import__("loadque").loadque
copyque = __import__("initque").copyque
checkque = __import__("checkque").checkque
showans = __import__("showans").showans
realque = __import__("realque").petrealque
realans = __import__("realans").petrealans


PetCodeAssetsPath = os.getenv("PetCodeAssetsPath") or "../assets"


class App(object):
    """
    Pet Code
    - A simple program for practicing coding -

    Warning!
    Que Index and Basic input info:
    q(basic) q(index)

    Answer Index input info:
    a(index)
    """

    def __init__(self, assets_path: str = PetCodeAssetsPath):
        self.assets = assets_path

    def listque(self, pages: int = 1, group_size: int = 20):
        """
        List Que at assets/index
        """

        listque(pages=pages, group_size=group_size,
                assets_path=self.assets)

    def listans(self, basic: str, index: str):
        """
        List Ans at Que

        Args:
            basic: str   # Index (Like q00)
            index: str   # Index (Like q000001)
        """

        realque(basic=basic, index=index, assets_path=self.assets)

        listans(basic=basic, index=index, assets_path=self.assets)

    def loadque(self, basic: str, index: str):
        """
        Load Que at assets/que

        Args:
            basic: str   # Index (Like q00)
            index: str   # Index (Like q000001)
        """

        realque(basic=basic, index=index, assets_path=self.assets)

        loadque(basic=basic, index=index, assets_path=self.assets)

    def initque(self, basic: str, index: str, output: str):
        """
        Init Que
        Copy Que's source file to output

        Arhs:
            basic : str    # Index (Like q00)
            index : str    # Index (Like q000001)
            output: str    # Output file (Like a.py)
        """

        realque(basic=basic, index=index, assets_path=self.assets)

        copyque(basic=basic, index=index,
                output=output, assets_path=self.assets)

    def checkque(self, basic: str, index: str, ansfile: str):
        """
        Check Que
        Real Answer?

        Args:
            basic  : str    # Index (Like q00)
            index  : str    # Index (Like q000001)
            ansfile: str    # Output file (Like a.py)
        """

        realque(basic=basic, index=index, assets_path=self.assets)

        checkque(basic=basic, index=index,
                 ansfile=ansfile, assets_path=self.assets)

    def showans(self, basic: str, index: str, ansindex: str):
        """
        Show Ans
        cat.exe Que's answer (bushi)

        Ars:
            basic   : str    # Index (Like q00)
            index   : str    # Index (Like q000001)
            ansindex: str    # Output file (Like a00)
        """

        realque(basic=basic, index=index, assets_path=self.assets)
        realans(basic=basic, index=index,
                ansindex=ansindex, assets_path=self.assets)

        showans(basic=basic, index=index,
                ansindex=ansindex, assets_path=self.assets)


if __name__ == "__main__":
    app = App()
    fire(app)
