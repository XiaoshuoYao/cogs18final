import pytest

import requests
from bs4 import BeautifulSoup
import re

from functions import process_url

def ProcessUrlTest():
    assert process_url() == ['https://ucsdnews.ucsd.edu/archives','https://ucsdnews.ucsd.edu/archives/P10']
    assert type(process_url()) == list