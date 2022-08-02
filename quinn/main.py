from multiprocessing.context import assert_spawning
import fire
import questionary
import sys
from pathlib import Path
import pandas as pd


from utils.calculators import (
    avg_price,
    std
)
from utils.utils import (
    enter_zip,
    get_bath,
    get_bed
)


def run():
    zip = enter_zip()
    bath = get_bath()
    bed = get_bed()

