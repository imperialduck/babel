from pip._vendor import requests


def get(url):
    user_agent_text = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
    headerdict = {"User-Agent": user_agent_text}
    html = requests.get(url, headers=headerdict)
    html.raise_for_status()
    return html


def get_urls(arglist, is_verbose=False):
    for url_en_arg in arglist:
        try:
            html = get(url_en_arg)
        except Exception as e:
            print(f"Erreur de request vers {url_en_arg}")
            print(str(e))
            html = None
        if html:
            displayurl(html)


def displayurl(html, is_verbose=False):
    print(f"--> Il y a {len(html.text)} octets dans {html.url}")
    if is_verbose:
        print("Statut :", html.status_code)
        print("Headers :", html.headers)
        print("Text :", html.text)
        for key, value in html.headers:
            print(f"{key} : {value}")


if __name__ == "__main__":
    listedesurls = ["matin", "midi", "soir", "minuit", "aube"]
    for item in listedesurls:
        print(item)
    listedesurls = [
        "http://www.legorafi.fr",
        "https://www.twitch.tv/",
        "https://github.com/Bebounet/babel-bebounet/blob/develop-bebounet/.gitignore",
    ]
    get_urls(listedesurls)
