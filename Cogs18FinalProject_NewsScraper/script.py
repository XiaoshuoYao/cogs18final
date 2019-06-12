import sys
sys.path.append('../')

import requests
from bs4 import BeautifulSoup
import re


from my_module.functions import MakeaSoup, process_url, GetLinks, SingleLink, GetArti, ProcessArti


start_page = input("Please type in a page number you want to start collect:\t")

#This module checks that if the input is a number
#if not, the user will be asked to do a input again
while start_page is not None:
    try:
        x = int(start_page)
        break
    except ValueError:
        print("Sorry but you have to type in a number")
        start_page = input("Please type in a page number you want to start collect:\t")
              
end_page = input("Please type in a page number you want to end collect:\t")

#This module checks that if the input is a number,
#if not, the user will be asked to do a input again
while end_page is not None:
    try:
        x = int(end_page)
        break
    except ValueError:
        print("Sorry but you have to type in a number")
        end_page = input("Please type in a page number you want to end collect:\t")

#This module checks that if the inputs is right for the program
if int(end_page) <= int(start_page):
    raise ValueError("The end page should larger than the start page")  
if int(end_page) > 516:
    raise ValueError("The page number exeed the page exists")

pages = process_url(int(start_page), int(end_page))

arti_links = []
proc_artilinks = []

for page in pages:
    arti_links.append(SingleLink(page))


for link in arti_links:
    proc_artilinks = proc_artilinks + link

count = 1

for link in proc_artilinks:
    texts = ProcessArti(link)
    filename = "NewsArticles\ UCSD_News_Article" + str(count) + ".txt"
    count = count + 1
    ArticleFile = open(filename,'w',encoding="utf-8")
    ArticleFile.write(texts)
    ArticleFile.close()

print("Finished! The files are in the NewsArticles folder.")