# Import necessary libraries
import fire
import questionary
import sys
from pathlib import Path
import pandas as pd


from utils.calculators import (
    calculations
)
from utils.utils import (
    enter_zip,
    get_accommodations,
    get_beds,
    get_nights
)


def run():
    """The main function for running the application"""
    # Take in the zip code from the user
    zipcode = enter_zip()

    bedrooms = get_beds()
    guests = get_accommodations()
    nights = get_nights()


    average,stddev = calculations(zipcode, bedrooms, guests)

    print(f'Based on your selected criteria, you should expect to spend around ${nights*average:.2f}.')
    print(f'You can expect to pay between ${nights*(average - stddev):.2f} and ${nights*(average + stddev):.2f}')


if __name__ == "__main__":
    fire.Fire(run)