from Crawler.DbFunctions import GetDb, CreateTextDB, InsertText, GetAllText
from Indexing.ProcessHtmlForIndexing import processHtmlForIndexing


def dbHtmlToText(dbName):
    db = GetDb(dbName)
    CreateTextDB()
    textDb = GetAllText()
    if(len(textDb) == len(db)):
        print("Html already parsed")
        return textDb
    dbProcessed = []
    i = 0
    for row in db:
        processedText = processHtmlForIndexing(row[1])
        dbProcessed.append((row[0],processedText))
        i +=1
        InsertText(row[0],processedText)
        print(f"Html to text on {i} items")
        if(i == 1000):
            break
    return dbProcessed