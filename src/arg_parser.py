"""
    Module for the Parsing of the given arguments
"""

#===== IMPORTS =======================================
import argparse

#===== FUNCTIONS =====================================
def parse_args():
    """
    Function that parses the command line arguments
    
    The return value is a complex object that holds the given arguments as directly accessible properties
    return - {obj} - args
"""
    
    # Generate parser Object
    parser = argparse.ArgumentParser()

    parser.add_argument('--market-id', type=str, help='Market ID, needs to be obtained by executing --list-markets.')
    parser.add_argument('--list-markets', type=str, help='Given the zip code (PLZ), list all markets and their ID.')
    parser.add_argument("--DEBUG", action="store_const", const=True, help="Set this flag if you want to perform the query live in terminal manually")

    # Get given parameters
    args = parser.parse_args()

    return args