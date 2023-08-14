# scraper.py
import requests
from bs4 import BeautifulSoup


def parse_website(url: str) -> type(BeautifulSoup):
    """
    Gets webpage content in HTML format
    :param url: webpage to parse
    :return: html structure in str format
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.find_all(text=True)

    output = ''

    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script'
    ]
    for paragraph in text:
        if paragraph.parent.name not in blacklist:
            output += '{}'.format(paragraph) + '\n'
    return output
