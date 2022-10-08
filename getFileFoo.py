import requests
import subprocess
import time


def downloadFile(URL):
    """This is the download file function."""
    debug = True
    if debug:
        print("In downloadFile")

    result = subprocess.run(['curl', "-L", '--url', URL, '-o', 'temp_221007-052009.html'], stdout=subprocess.PIPE, shell=True, text=True)
    ts = time.time()
    if debug:
        print(ts)
        print("Leaving downloadFile with result code : " + str(result))

    #todo auto set date and time on test file.
    #todo clean up returned results to simple true false.


def fetchHTML(URL):
    """
    Given :
    Downloads the data from the URL.
    :return: Confirmation that raw data has been successfully downloaded and saved.
    """
    downloadFile(URL)
    #ToDo : add in validation here.


def fetchURL():
    """
    This is stub code that currently just returns a hardcoded url.
    :return: URL string.
    """
    return "https://binghamton.craigslist.org/search/berkshire-ny/mca?lat=42.2899%26lon=-76.2076%26max_price=%26min_price=%26query=BMW%26search_distance=34"


def main():
    print("In getFileFoo.py Main")

if __name__ == "__main__":
    main()