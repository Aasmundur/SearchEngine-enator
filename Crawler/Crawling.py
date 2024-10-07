from Crawler.CrawlerFrontier import add_url_to_frontier, get_next_url, get_size_of_frontier
from Crawler.HelperFunctions import is_valid_url
from Crawler.Fetchsite import fetch_single_site
from Crawler.DbFunctions import CreateHtmlUrlDb, InsertHtmlUrl, GetDb
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup

CreateHtmlUrlDb("UrlHtmlDb.db")

seed = ["https://www.bbc.com/news", "https://www.dr.dk/", "https://nyheder.tv2.dk/"]

MAX_PAGES = 4000

def extract_links(html, base_url):
    """Extracts all valid links from the given HTML and converts them to absolute URLs."""

    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href'].strip()
        # Convert relative URLs to absolute URLs
        link = urljoin(f"{base_url.scheme}://{base_url.netloc}", link)

        if not is_valid_url(link):
            continue

        links.add(link)
    
    return links

def Crawler():
    pages_crawled = 0
    crawledPagesFromDb = GetDb("UrlHtmlDb.db")
    pages_crawled = len(crawledPagesFromDb)
    crawled_urls = [entry[0] for entry in crawledPagesFromDb]
    for url in seed:
        add_url_to_frontier(url)
    iters = 0
    already_crawled_number = 0
    while pages_crawled < MAX_PAGES:
        print(f"Pages crawled: {pages_crawled}")
        url = get_next_url()
        print(url)
        if not url:
            print("No more URLs to crawl.")
            break
        parsed_url = urlparse(url)
        url, html = fetch_single_site(url)
        if not html:
            continue
        iters +=1
        if url in crawled_urls and iters > 1:
            pages_crawled += 1
            already_crawled_number += 1
            continue
        # Process the page
        InsertHtmlUrl("UrlHtmlDb.db", url, html)
        print(f"Crawled {url}")
        pages_crawled += 1

        # Extract and add new links to the frontier
        new_links = extract_links(html, parsed_url)
        for link in new_links:
            parsed_link = urlparse(link)
            if("google" not in parsed_link.netloc and
                "blog" not in parsed_link.netloc and
                "developer" not in parsed_link.netloc and
                "dev" not in parsed_link.netloc and
                "apple" not in parsed_link.netloc):
                add_url_to_frontier(link, parsed_url=parsed_link)
        print("frontier size: ", get_size_of_frontier())
        if pages_crawled >= MAX_PAGES:
            (f"Reached the maximum limit of {MAX_PAGES} pages.")
            break
