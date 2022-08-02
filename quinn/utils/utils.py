import sys
import questionary
import fire

def enter_zip():
    zip = questionary.text('Enter the zip code for the neighborhood you would like to research').ask()
    zip = int(zip)
    if len(zip) > 5 or len(zip) < 5:
        print(f'The zip code must be 5 digits')
        sys.exit()
    elif type(zip) != int:
        print(f'The zip code must be numbers')
        sys.exit()
    else:
        return zip 
# Need to check and see if zip is part of df if not we need to print error

def get_bath():
    bath = questionary.select(
        'How many bathrooms are you looking for?',
        choices=[
            '0.5',
            '1',
            '1.5',
            '2',
            '2.5',
            '3',
            '3.5',
            '4',
            '4.5',
            '5'
        ]
    ).ask()
    return bath



def get_bed():
    bed = questionary.select(
        'How many bedrooms are you looking for?',
        choices=[
            '1',
            '2',
            '3',
            '4',
            '5'
        ]
    ).ask()
    return bed



