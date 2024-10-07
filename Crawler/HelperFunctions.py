import time, requests
from urllib.parse import urlparse
from RobotsParser.Functions.parse_robots_txt import parse_robots_txt
host_robots_rules = {}

def wait_if_needed(host, host_last_access, default_delay=2):
    """Wait if the host was accessed recently, enforcing politeness."""
    crawl_delay = get_crawl_delay(host) or default_delay
    last_access = host_last_access.get(host, 0)
    time_since_last_access = time.time() - last_access
    if time_since_last_access < crawl_delay:
        time.sleep(crawl_delay - time_since_last_access)

def get_crawl_delay(host):
    """Return the crawl delay for a given host based on robots.txt (default is None)."""
    robots_rules = host_robots_rules.get(host, None)
    if robots_rules:
        for rule in robots_rules:
            if rule.user_agent == "*":
                return rule.crawl_delay
    return None

def get_main_domain(host):
    parts = host.split('.')
    if len(parts) > 2:
        return '.'.join(parts[-2:])  
    return host

def obey_robots_txt(url):
    """Check if the URL is allowed according to robots.txt."""
    parsed_url = urlparse(url)
    host = get_main_domain(parsed_url.netloc)
    path = parsed_url.path

    if host not in host_robots_rules:
        robots_url = f"{parsed_url.scheme}://{host}/robots.txt"
        try:
            host_robots_rules[host] = parse_robots_txt(robots_url)
        except requests.exceptions.RequestException as e:
            print(f"Could not fetch robots.txt for {host}: {e}")
            host_robots_rules[host] = []
            return True
    robots_rules = host_robots_rules[host]
    for rule in robots_rules:
        if rule.user_agent == '*' and any(path.startswith(disallowed) for disallowed in rule.disallows):
            return False

    return True

def is_valid_url(link):
    """Filter out URLs that are not valid HTML links (e.g., deep links, file URLs)."""
    invalid_extensions = ('.pdf', '.jpg', '.png', '.zip', '.exe', '.xml', '.apk', '.gif')
    if any(link.endswith(ext) for ext in invalid_extensions):
        return False
    
    parsed_link = urlparse(link)
    # Filter out links to known deep-linking services or non-web domains
    if 'page.link' in parsed_link.netloc:
        return False
    
    # Further filtering logic can be added here (e.g., by domain or path structure)
    return True