import pprint
import time
from operator import index

from Indexing.dbHtmlToText import dbHtmlToText
from NearDuplicatesFunctions.NearDuplicates import NearDuplicates
from Ranking.PageRank import PageRank
from RobotsParser.Functions.parse_robots_txt import parse_robots_txt
from Crawler.Fetchsite import fetch_single_site
from Crawler.Crawling import Crawler
from Crawler.DbFunctions import GetDb
from Indexing.indexing import indexer
from Indexing.ProcessHtmlForIndexing import processHtmlForIndexing
from Indexing.dbHtmlToText import dbHtmlToText
from Querying.ProcessQuery import ProcessQuery
def main():
    # Crawler()
    # dbProcessed = dbHtmlToText("UrlHtmlDb.db")
    # term_dict, doc_id_to_url= indexer(dbProcessed)
    # term_dict = {
    #     "aalborg": (4, [(2, 2), (3, 1), (9, 3), (13, 1)]),
    #     "university": (4, [(1, 1), (2, 2), (3, 1), (5, 1)]),
    #     "engineer": (3, [(1, 1), (3, 1), (7, 2)]),
    #     "computer": (2, [(2, 1), (4, 2)]),
    #     "science": (3, [(1, 2), (2, 1), (4, 1)]),
    #     "denmark": (2, [(1, 1), (5, 1)]),
    #     "student": (3, [(2, 1), (3, 2), (5, 1)]),
    #     "research": (2, [(3, 1), (4, 1)]),
    #     "technology": (3, [(1, 1), (2, 2), (4, 1)])
    # }
    #
    # # # Example doc_id_to_url
    # doc_id_to_url = {
    #     "https://www.aau.dk": 1,
    #     "https://www.cs.aau.dk": 2,
    #     "https://www.en.aau.dk": 3,
    #     "https://www.engineering.aau.dk": 4,
    #     "https://www.studyindenmark.dk/study-options/danish-higher-education-institutions/universities/aalborg-university": 5,
    #     "asfgsdfdsda": 7,
    #     "gsadas": 9,
    #     "sdadadad": 13
    # }
    # ProcessQuery(term_dict, doc_id_to_url)
    PageRank()
if __name__ == "__main__":
    main()