# scraper.py
# simple web scraper for FE 595 HW2


# modules
import re
import requests
from bs4 import BeautifulSoup


# extract the company name and company purpose
def extract_name_purpose(url, err_mesg=True):
    """

    extract the company name and purpose from url

    :param url: the http address
    :param err_mesg: whether to print our the error message
    :return: status(booleans): True or False, whether the scraper is successful
            data(dictionary): the dictionary for company name and purpose. If the status is false, return a empty dict.
    """

    # make a request
    try:
        resp = requests.get(url)
        resp.raise_for_status()
    except requests.exceptions.HTTPError:
        if err_mesg:
            print(str(resp.status_code) + ' ' + requests.status_codes._codes[resp.status_code][0])
        return False, dict()

    # parse the html file
    parsed_resp = BeautifulSoup(resp.text, 'html.parser').getText()

    # search for company name
    name = re.compile(r'Name: .+').search(parsed_resp).group()
    name = re.sub(pattern=r'Name: ', repl='', string=name)

    # search for company purpose
    purpose = re.compile(r'Purpose: .+').search(parsed_resp).group()
    purpose = re.sub(pattern=r'Purpose: ', repl='', string=purpose)

    # return
    return True, {'Name': name, 'Purpose': purpose}
