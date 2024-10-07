from RobotsParser.Classes.RobotsRule import RobotsRule
import requests

def parse_robots_txt(url): 
    response = requests.get(url)
    response.raise_for_status()
    lines = [line.split('#')[0].strip() for line in response.text.splitlines() if line.strip()]
    
    rules = []
    current_agents = []

    for line in lines:
        if line.lower().startswith('user-agent:'):
            current_agents = [line.split(':', 1)[1].strip()]  # Reset for each User-agent
        elif any(line.lower().startswith(prefix) for prefix in ['allow:', 'disallow:', 'crawl-delay:', 'sitemap:']):
            apply_rule_to_agents(line, current_agents, rules)

    return rules

def apply_rule_to_agents(line, agents, rules):
    key, value = line.split(':', 1)
    value = value.strip()

    for agent in agents:
        # Search if agent rule already exists
        rule = next((r for r in rules if r.user_agent == agent), None)
        if rule is None:
            rule = RobotsRule(agent)
            rules.append(rule)

        if key.lower() == 'allow':
            rule.allows.append(value)
        elif key.lower() == 'disallow':
            rule.disallows.append(value)
        elif key.lower() == 'crawl-delay':
            rule.crawl_delay = int(value)
        elif key.lower() == 'sitemap':
            rule.sitemaps.append(value)
