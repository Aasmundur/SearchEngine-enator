import random
from Crawler.DbFunctions import GetDb
from bs4 import BeautifulSoup
from tabulate import tabulate
import re
def ExtractLinksThatAreAlsoInDb (html, db):
    links = []
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a',
                              attrs={"href": re.compile("^https://")}):
        url = link.get('href')
        if any(url == entry[0] for entry in db):
            links.append(url)
    return links
def CreateTransitionProbMatrix():
    db = GetDb("UrlHtmlDb.db")
    urlAndIdDict = {}
    id = 0
    for entry in db:
        print(f"Extracted links for {id} urls")
        urlAndIdDict[id] = (entry[0],ExtractLinksThatAreAlsoInDb(entry[1], db))
        id = id + 1
    transitionProbMatrix = [[0 for _ in range(len(urlAndIdDict))] for _ in range(len(urlAndIdDict))]
    for row in range(len(urlAndIdDict)):
        links = urlAndIdDict[row][1]
        denominator = len(links)
        for col in range(len(urlAndIdDict)):
            probability = 0
            if(row == col):
                transitionProbMatrix[row][col] = probability
                continue
            if(denominator == 0):
                probability = 0
            else:
                col_url = urlAndIdDict[col][0]
                if col_url in links:
                    probability = 1/denominator
            transitionProbMatrix[row][col] = probability
    return transitionProbMatrix


def PowerIterations(transitionProbMatrix, probabilityDist):
    transitionProbMatrix = [[0.7, 0.3], [0.4, 0.6]]
    probabilityDist = [1, 0]

    result = MultiplyMatrices(transitionProbMatrix, probabilityDist)
    print(f"dist: {tabulate([probabilityDist])}")
    print(f"transProb: {tabulate(transitionProbMatrix)}")
    print(f"result: {tabulate([result])}")
    return

def MultiplyMatrices(transitionProbMatrix, probabilityDist):
    result = [0 for _ in range(len(transitionProbMatrix))]

    for i in range(len(transitionProbMatrix)):
        for j in range(len(probabilityDist)):
            result[i] += transitionProbMatrix[i][j] * probabilityDist[j]

    return result


def PageRank ():
    # transitionProbMatrix = CreateTransitionProbMatrix()
    # randNum = random.randint(0,len(transitionProbMatrix[0]))
    # probabilityDist = [0]*len(transitionProbMatrix[0])
    # probabilityDist[randNum] = 1
    # PowerIterations(transitionProbMatrix, probabilityDist)
    PowerIterations(None, None)
    # links = ExtractLinks(db[:1][0][1])
    # print(links)
