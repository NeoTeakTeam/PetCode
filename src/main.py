#!python3

from fire import Fire as fire
import json
import sys
import io
import shutil as sl

import listque
import loadque
import initque
import checkque
import showans


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
        List Que at ../assets/index
        """

        listque.listque()

    def loadque(self, basic: str, index: str):
        """
        Load Que at ../assets/que

        Args:
            basic: str   # Index (Like q00)
            index: str   # Index (Like q000001)
        """

        loadque.loadque(basic=basic, index=index)

    def initque(self, basic: str, index: str, output: str):
        """
        Init Que
        Copy Que's source file to output

        Arhs:
            basic : str    # Index (Like q00)
            index : str    # Index (Like q000001)
            output: str    # Output file (Like a.py)
        """

        initque.copyque(basic=basic, index=index, output=output)

    def checkque(self, basic: str, index: str, ansfile: str):
        """
        Check Que
        Real Answer?

        Args:
            basic  : str    # Index (Like q00)
            index  : str    # Index (Like q000001)
            ansfile: str    # Output file (Like a.py)
        """

        checkque.checkque(basic=basic, index=index, ansfile=ansfile)

    def showans(self, basic: str, index: str, ansindex: str):
        """
        Show Ans
        cat.exe Que's answer (bushi)

        Ars:
            basic   : str    # Index (Like q00)
            index   : str    # Index (Like q000001)
            ansindex: str    # Output file (Like a00)
        """

        showans.showans(basic=basic, index=index, ansindex=ansindex)


if __name__ == "__main__":
    app = App()
    fire(app)
