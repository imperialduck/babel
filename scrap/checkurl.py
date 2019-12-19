from pip._vendor import requests
# html = requests.get("https://www.liberation.fr/")
# print("Statut :", html.status_code)
# print("Headers :", html.headers)
# print("Text :", html.text)
# html = requests.get("http://localhost:8080/formext/avions/avions")
# print("Statut :", html.status_code)
# print("Headers :", html.headers)
# print("Text :", html.text)


def get(url):
    user_agent_text = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
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
        "http://localhost:8080/formext/avions/avions",
        "https://www.dealabs.com/nouveaux",
        "https://github.com/Bebounet/babel-bebounet/blob/develop-bebounet/.gitignore",
    ]
    get_urls(listedesurls)