"""
    Preparing a WebScraper for the current offers
    at REWE using their web-based API

    author:     Alexander Müller
    date:       04.11.2022
    version:    0.0.1
    
"""


#===== LIBRARIES =====================================
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

#===== IMPORTS =======================================
import json

#===== MODULES =======================================
from src.arg_parser import parse_args
from src.terminal_info import info, error

#===== FUNCTIONS =====================================
def get_list_of_markets(plz=86159):

    # Build URL
    url = f"https://shop.rewe.de/mc/api/markets-stationary/{plz}"

    # Build Webdriver to access without Bot Prevention
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # Load the Page
    driver.get(url)

    # Parse the JSON
    content = driver.page_source
    market_list = content.split('<div id="json">')
    market_list = json.loads(market_list[1].split("</div>")[0])

    # Close the Browser
    driver.quit()

    return market_list


def get_current_offers(market_id=441050):
    """
    Request the JSON with the current offers and prices

    param - {int} - market_id - TODO could be an str coming from JSON

    return - {dict} - current_offers
    """

    # Build URL
    url = f"https://mobile-api.rewe.de/api/v3/all-offers?marketCode={market_id}"

    # Build Webdriver to access without Bot Prevention
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # Load the Page
    driver.get(url)

    # Parse the JSON
    content = driver.page_source
    current_offers = content.split('<div id="json">')
    current_offers = json.loads(current_offers[1].split("</div>")[0])
    print(json.dumps(current_offers, indent=4))

    # Close the Browser
    driver.quit()

    return current_offers

#===== MAIN ==========================================
if __name__ == "__main__":

    # Get args
    args = parse_args()

    # Get market list near given PLZ
    if args.list_markets:

        # Get postal code
        plz = args.list_markets

        info(f"Listing all market for PLZ: {plz}")
        market_list = get_list_of_markets(plz=plz)

        # List of three nearest markets
        market_list = market_list["stationaryMarkets"][0:3]
        
        # Routine for manual mode
        if args.DEBUG:

            for index, market in enumerate(market_list):
                print(f'[{index+1}]\t{market["id"]}\t{market["name"]}\t{market["address"]["city"]}')

            # For manual mode: asks if user wants to select the market
            selected_market = int(input("Which market do you want to look into? [1,3]\t"))-1

            current_offers = get_current_offers(market_id=market_list[selected_market]["id"])

    
    # Get the current offers from the selected market
    else:
        current_offers = get_current_offers(market_id=args.market_id)

        # Parse the current offers to a custom JSON and store with according store information