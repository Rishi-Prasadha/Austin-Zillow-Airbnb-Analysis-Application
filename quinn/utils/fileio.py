import fire
import questionary
import sys
from pathlib import Path
import pandas as pd


def read_csv(csvpath):
    csvpath = Path('Resources/')
