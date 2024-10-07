from Querying.Complement import Complement
from Querying.Intersect import intersect
from Querying.ProcessAnd import ProcessAnd
from Querying.ProcessNot import ProcessNot
from Querying.ProcessOr import ProcessOr
from nltk.stem import PorterStemmer


def ProcessQuery(term_dict, doc_id_to_url):
    query = input('Enter your query:\n')
    query_terms= list()
    query_terms_notstemmed = query.lower().split()

    stemmer = PorterStemmer()

    for term in query_terms_notstemmed:
            if term != "or" and term != "and" and term != "not":
                stemmed_term = stemmer.stem(term)
                query_terms.append(stemmed_term)
    print(query_terms)
    terms = []
    operators = []
    all_doc_ids = set(doc_id_to_url.values())  # Set of all document IDs

    i = 0
    while i < len(query_terms):
        if query_terms[i] == 'not':
            if i + 1 < len(query_terms):
                next_term = query_terms[i + 1]
                if next_term in term_dict:
                    not_posting = ProcessNot(term_dict[next_term][1], all_doc_ids)
                    terms.append(not_posting)
                else:
                    print(f"Error: term '{next_term}' not found.")
                    return set()
                i += 2  # Skip 'not' and the following term
            else:
                print("Error: 'NOT' must be followed by a term.")
                return set()
        elif query_terms[i] in ['and', 'or']:
            operators.append(query_terms[i])
            i += 1
        else:
            if query_terms[i] in term_dict:
                doc_ids = set(doc_id for doc_id, _ in term_dict[query_terms[i]][1])
                terms.append(doc_ids)
            else:
                terms.append(set())  # Empty set if term not found
            i += 1

    # Process 'OR' operators first (joining all ORs)
    if 'or' in operators:
        result = ProcessOr([terms[i] for i in range(len(terms)) if i == 0 or operators[i - 1] == 'or'])
        terms = [result]  # Use the result of OR as a single term for further processing
        operators = [op for op in operators if op != 'or']  # Remove ORs for the next stage

    # Sort the remaining AND terms by increasing document frequency (posting list size)
    and_terms = sorted(terms, key=len)

    # Process the remaining 'AND' operators
    if and_terms:
        result = ProcessAnd(and_terms)

    # Print results
    if result:
        print(f"Found {len(result)} documents:")
        for doc_id in result:
            for url, id in doc_id_to_url.items():
                if id == doc_id:
                    print(f"Document ID: {doc_id}, URL: {url}")
    else:
        print("No documents found matching the query.")

    return result

