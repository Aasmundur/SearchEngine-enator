import re
from bs4 import BeautifulSoup, Tag

def processHtmlForIndexing(html):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Extract text from specific tags
    title = soup.find('title')
    title_text = title.get_text(strip=True) if title else ""

    # Find all paragraph tags
    paragraphs = soup.find_all('p')
    paragraph_texts = [p.get_text(strip=True) for p in paragraphs]

    # Find all heading tags (h1 to h6)
    headings = soup.find_all(re.compile('^h[1-6]$'))
    heading_texts = [h.get_text(strip=True) for h in headings]

    # Combine all extracted text
    all_text = [title_text] + heading_texts + paragraph_texts

    # Join all text elements with newlines
    result = '\n'.join(filter(None, all_text))

    return result