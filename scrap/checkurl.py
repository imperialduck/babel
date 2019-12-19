from pip._vendor import requests
import json
import os
from bs4 import BeautifulSoup

dataset = []


def printseparator():
    """ Fonction qui affiche une ligne de séparation """
    print("-" * 50)


F_URL = "url"
F_STATUS = "status_code"
F_HTML = "content"
F_TITLE = "title"


def writetodict(html, is_verbose):
    title = search_title_by_soup(html.text)
    dict = {F_URL: html.url, F_STATUS: html.status_code, F_HTML: html.text[:1000], F_TITLE: title}
    global dataset 
    dataset.append(dict)


def search_title_by_soup(text):
    soup = BeautifulSoup(text, "lxml")
    return soup.title.string


def search_title(text):   
    retbuffer = begin = 0
    end = None
    begin = text.find("<title>")
    if begin != -1:
        begin += len("<title>")
        end = text[begin:].find("</title>")
        if end != -1:
            end += begin
            retbuffer = text[begin:end]
    print(f"Test search_title: {begin}, {end}, {retbuffer}")
    return retbuffer


def get(url):
    user_agent_text = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
    headerdict = {"User-Agent": user_agent_text}
    html = requests.get(url, headers=headerdict)
    html.raise_for_status()
    return html


def get_urls(arglist, is_verbose=True):
    """ recuperer tout les urls listés dans listedesurls[ ] """
    for url_en_arg in arglist:
        try:
            html = get(url_en_arg)
        except Exception as e:
            print(f"Erreur de request vers {url_en_arg}")
            print(str(e))
            html = None
        if html:
            displayurl(html, is_verbose)
            writetodict(html, is_verbose)


def displayurl(html, is_verbose):
    print(f"--> Il y a {len(html.text)} octets dans {html.url}")
    if is_verbose:
        printseparator()
        print("Statut :", html.status_code)
        printseparator()
        print("Headers :", html.headers)
        printseparator()
    else:
        print(f"Erreur de request vers {html.url} ---- avec code : {html.status_code}")
        for key, value in html.headers.items():
            print(f"{key} : {value}")

    
if __name__ == "__main__":
    urls = ["http://www.legorafi.fr", "https://www.systemrequirementslab.com/cyri", "https://imgur.com/"]
    get_urls(urls, False)
    print(len(dataset))
    print(__file__)
    filedir = (os.path.abspath(__file__))
    print(filedir)
    basedir = (os.path.dirname(filedir))
    print(basedir)
    filename = basedir + "/checkurl.json"
    # with permet d'éviter de faire close("test.json"... etc)
    with open(filename, "w", encoding="utf8") as f:
        json.dump(dataset, f)  # prend un objet python et un handle de fichier et écrit dedans
