class RobotsRule:
    def __init__(self, user_agent):
        self.user_agent = user_agent
        self.allows = []
        self.disallows = []
        self.crawl_delay = None
        self.sitemaps = []

    def __repr__(self):
        return f"<UserAgent: {self.user_agent}, Allows: {self.allows}, Disallows: {self.disallows}, Crawl-delay: {self.crawl_delay}, Sitemaps: {self.sitemaps}>"