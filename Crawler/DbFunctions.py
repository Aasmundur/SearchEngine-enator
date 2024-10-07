import sqlite3

def GetAllText(dbName="textDb.db"):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    try:
        # Retrieve all rows from the textDb table
        cursor.execute('SELECT url, text FROM textDb')
        rows = cursor.fetchall()

        return rows

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        conn.close()

def InsertText(url, processedText, dbName="textDb.db"):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    try:
        # Insert URL and processed text into the textDb table
        cursor.execute('''
            INSERT INTO textDb (url, text)
            VALUES (?, ?)
        ''', (url, processedText))

        conn.commit()
        print(f"URL '{url}' and text successfully inserted into the database.")

    except sqlite3.IntegrityError:
        print(f"URL '{url}' already exists in the database.")

    finally:
        conn.close()

def CreateTextDB(db_name="textDb.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS textDb (
            url TEXT NOT NULL UNIQUE,
            text TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def CreateHtmlUrlDb(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS UrlHtml (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL UNIQUE,
                html TEXT NOT NULL
            )
        ''')
    conn.commit()
    conn.close()

def InsertHtmlUrl(dbName, url, html):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    if not url or not html:
        return
    try:
        # Insert URL and its filtered HTML content into the UrlHtml table
        cursor.execute('''
                INSERT INTO UrlHtml (url, html)
                VALUES (?, ?)
            ''', (url, html))

        conn.commit()
    except sqlite3.IntegrityError:
        print(f"URL '{url}' already exists in the database.")
    finally:
        conn.close()

def GetDb(dbName):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    # Select all records from the UrlHtml table
    cursor.execute('SELECT url, html FROM UrlHtml')

    rows = cursor.fetchall()

    conn.close()

    return rows
