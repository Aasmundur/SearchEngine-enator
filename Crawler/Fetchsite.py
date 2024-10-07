
import requests
import time
from urllib.parse import urlparse
from Crawler.HelperFunctions import wait_if_needed, obey_robots_txt
from Crawler.FilterHtml import FilterHtml


# Dictionary to keep track of last access times and crawl delays
host_last_access = {}

def fetch_single_site(url):
    """Fetch a single site and return (url, html) as a tuple, obeying politeness rules."""
    parsed_url = urlparse(url)
    host = parsed_url.netloc

    wait_if_needed(host, host_last_access)

    if not obey_robots_txt(url):
        return None, None
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None, None
    html = FilterHtml(response.text)
    host_last_access[host] = time.time()
    return url, html

