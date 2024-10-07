import nltk
from collections import defaultdict
from nltk.stem import PorterStemmer



# def indexer():
#     docs = [doc1, doc2, doc3, doc4]
#     inverted_index = defaultdict(lambda: {'doc_ids': [], 'doc_freq': 0})
#
#     for doc_id, doc in enumerate(docs, start=1):
#         terms = tokenizer(doc)
#         unique_terms = set(terms)
#
#         for term in unique_terms:
#             if doc_id not in inverted_index[term]['doc_ids']:
#                 inverted_index[term]['doc_ids'].append(doc_id)
#                 inverted_index[term]['doc_freq'] += 1  # Increment the document frequency for the term
#     print(inverted_index)
#     return inverted_index

def indexer(docs):
    doc_term_array = []
    doc_id_to_url = {}
    for i, doc in enumerate(docs, start=1):
        url, _ = doc
        doc_id_to_url[url] = i
    for doc in docs:
        doc_id, text = doc
        terms = tokenizer(text)
        term_counts = defaultdict(int)
        for term in terms:
            term_counts[term.lower()] += 1
        for term, count in term_counts.items():
            doc_term_array.append((term, doc_id_to_url[doc_id], count))
    doc_term_array.sort(key=lambda x: (x[0],x[1]))
    term_postings = defaultdict(list)
    term_doc_freq = defaultdict(int)
    for term, doc_id, term_freq in doc_term_array:
        term_postings[term].append((doc_id, term_freq))
    term_dict = {}
    for term, posting_list in term_postings.items():
        doc_freq = len(posting_list)
        term_dict[term] = (doc_freq, sorted(posting_list))
    print(f"Term dict: {term_dict}\n doc_id_to_url: {doc_id_to_url}")
    return term_dict, doc_id_to_url




def tokenizer(document):
    ps = PorterStemmer()
    documentArr = []
    documentArr = document.split()
    documentArr = [x.lower() for x in documentArr]
    documentArr = [ps.stem(x) for x in documentArr]
    return documentArr