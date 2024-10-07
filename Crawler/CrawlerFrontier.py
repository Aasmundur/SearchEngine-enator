from Crawler.HelperFunctions import is_valid_url
from heapq import heappop, heappush
from urllib.parse import urlparse
frontier = []
seen_urls = set()
seen_domains = {}
def add_url_to_frontier(url, priority=0, parsed_url=None):
    # Use the parsed URL if it's already provided, otherwise parse it
    if parsed_url is None:
        parsed_url = urlparse(url)
    
    if not is_valid_url(url):
        return

    domain = parsed_url.netloc
    if not domain:
        return
    # Adjust priority based on domain to avoid crawling one domain too much
    if domain in seen_domains:
        # Increment priority for domains already seen
        priority += seen_domains[domain]
    else:
        # Initialize priority for a new domain
        seen_domains[domain] = 0

    # Add the URL to the frontier if it hasn't been seen
    if url not in seen_urls:
        heappush(frontier, (priority, url))
        seen_urls.add(url)
        seen_domains[domain] += 1  # Increase count for this domain

def get_next_url():
    """Pop the next URL from the frontier."""
    if frontier:
        priority, url = heappop(frontier)
        return url
    return None

def get_size_of_frontier ():
    return len(frontier)