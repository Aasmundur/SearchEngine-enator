from bs4 import BeautifulSoup

def FilterHtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(['script', 'style']):
        script.decompose()
    return str(soup)