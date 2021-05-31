import requests
from bs4 import BeautifulSoup
import re


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_count(URL):

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    citations = soup.findAll('a', attrs = {'title' : re.compile(r"Wikipedia:Citation needed")})

    number_of_citations = len(citations)

    return number_of_citations



def get_citations_needed_report(URL):

    result = ''

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    all_p_tags = soup.find_all('p')  

    for paragraph in all_p_tags:

        a_tags = paragraph.findAll('a', attrs = {'title' : re.compile(r"Wikipedia:Citation needed")})

        if a_tags:

            result = result + (paragraph.text) + '\n'

    return result


print(get_citations_needed_count(URL))

print(get_citations_needed_report(URL))