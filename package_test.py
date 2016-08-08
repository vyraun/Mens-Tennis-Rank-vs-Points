# Preliminary Check for requirements. No guarantees.

import os
import math
import sys

def test_bs4():
    try:
        from bs4 import BeautifulSoup 
    except ImportError:
        print("Could not import BeautifulSoup -> Failed")
        return None


def test_matplotlib():
    try:
        import matplotlib.pyplot
    except ImportError:
            print("Could not import matplotlib -> Failed")
            return None
   
def test_pandas():
    try:
        import pandas
    except ImportError:
            print("Could not import pandas -> Failed")
            return None


if __name__ == "__main__":
    print("\nNo Failed Message means its Okay.")

    print("\nTesting BeautifulSoup."),
    test_bs4()

    print("\nTesting matplotlib."),
    test_matplotlib()

    print("\nTesting pytest.\n\n"),
    test_pandas()




