import fire
import sys
import questionary
import pandas as pd
from pathlib import Path

from utils.utils_v2 import *
from utils.calculations_v2 import *

def run():
    """The main function for running the script."""
    # Load the zip code from user
    zipcode = enter_zip()

    # Ask user for bedrooms and guests
    bedrooms = get_beds()
    guests = get_accomodations()

    # Run necessary calculations
    average, stddev = calculations(zipcode, bedrooms, guests)

    
    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
