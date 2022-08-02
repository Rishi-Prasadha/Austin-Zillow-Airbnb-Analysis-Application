# Import statements 

import fire
import sys
import questionary
import pandas as pd
from pathlib import Path

airbnb_data = pd.DataFrame(Path("../Resources/austin_airbnb_data.csv"))

def enter_zip():
    zip = questionary.text("Enter the zip code you're interested in staying in:").ask()
    zip = int(zip)
    if len(zip) > 5 or len(zip) < 5:
        print('Error: zip code must be 5 digits long')
        sys.exit()
    elif type(zip) != int:
        print("Error: zip code must be a number integer")
    else:
        included_zipcodes = airbnb_data['Zip Code'].tolist()
        for data in included_zipcodes:
            if zip == data:
                return zip
            else:
                print('Error: the zip code you requested cannot be identified')
                sys.exit()

def get_beds():
    beds = questionary.select("How many bedrooms would you like?",
    choices= [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6'
    ])
    return beds
    
def get_baths():    
    baths = questionary.select("How many bathrooms would you like?",
    choices= [
        '1',
        '1.5',
        '2',
        '2.5',
        '3',
        '3.5',
        '4',
        '4.5',
        '5'
    ])
    return baths