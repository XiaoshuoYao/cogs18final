import requests
from bs4 import BeautifulSoup
import re

def MakeaSoup(url):
    
    """Get the source code of a web page and save it to a BeautifulSoup type variable.
    
    Parameters
    ----------
    url : string
        String contains the hyperlink of the page we want to get
        
    Returns
    -------
    output : BeautifulSoup Object
        A beautifulSoup Object contains the source code of the url.
    """

    content = requests.get(url)
    output = BeautifulSoup(content.text,features="html.parser")

    return output


def process_url(start_page=1,end_page=2):
    
    """Produce the list of urls represent the pages from the start_page to the end_page.
    
    Parameters
    ----------
    start_page : int
        The number of the page you want to start.
        
    end_page: int
        The number of the page you want to end.
        
    Returns
    -------
    output_list : list
        A list contains the urls of the pages you want to get.
    """

    output_list = []
    counter = start_page
    default_url = "https://ucsdnews.ucsd.edu/archives"
    
    #Generate the urls and save them in a list
    while counter <= end_page:
        if counter - 1 == 0:
            output_list.append(default_url)
        else:
            output_list.append(default_url + "/P" + str((counter-1)*10))
        counter = counter + 1

    return output_list


def GetLinks(url):
    
    """Find all the links of articles in a page's source code.
    
    Parameters
    ----------
    url : string
        The link of the page to process.
        
    Returns
    -------
    output : list
        A list contains the hyperlinks of the articles in the page.
    """

    page = MakeaSoup(url)
    links = page.find_all("h2")
    output = []
    
    #Save the BeautifulSoup result object in a list
    for link in links:
        output.append(str(link))

    return output


def SingleLink(url):

    """Process the list of hyperlinks find by GetLinks.
    
    Parameters
    ----------
    url : string
        The link of the page to process.
        
    Returns
    -------
    output : list
        A processed list contains the hyperlinks of the articles in the page.
    """
    
    url_list = GetLinks(url)
    counter = 0
    output_list = []
    
    #Process the links and save them in a list
    while counter < len(url_list) - 1:
        proc_ele = url_list[counter].split('"')
        output_list.append(proc_ele[1])
        counter = counter + 1

    return output_list


def GetArti(url):
    
    """Find the article texts in a page's source code.
    
    Parameters
    ----------
    url : string
        The hyperlink of the page.
        
    Returns
    -------
    output : list
        A list contains the article texts in the page.
    """
    
    #Get article texts
    page = MakeaSoup(url)
    article = page.find_all("p")
    article_result = []
    
    #Save all the article texts in a list
    for element in article:
        article_result.append(str(element))

    return article_result

def ProcessArti(url):

    """Process the article text got by GetArti.
    
    Parameters
    ----------
    url : string
        The hyperlink of the page contains the article.
        
    Returns
    -------
    output2 : string
        A String contains the article texts, processed, easier to read.
    """
    
    proc_arti = GetArti(url)
    output = []
    output2 = ""
    counter = 0
    
    #Process the article, remove the elements affect reading
    for elements in proc_arti:

        progress_1 = elements.replace("<p>","")
        progress_2 = progress_1.replace("<em>","")
        progress_3 = progress_2.replace("</em>","")
        progress_4 = progress_3.replace("</p>","")
        progress_5 = progress_4.replace("<a>","")
        progress_6 = progress_5.replace("</a>","")
        progress_7 = progress_6.replace("<br/>","")
        progress_8 = progress_7.replace("\n"," ")
        progress_9 = progress_8.replace("\t","")
        progress_10 = progress_9.replace(">","")
        progress_11 = progress_10.replace("<i","")
        progress_12 = progress_11.replace("</i","")
        output.append(progress_12)

    #save the processed article from the list as a string
    while counter < len(output):
        output2 = output2 + output[counter]
        counter = counter + 1

    return output2
