import math
from collections import defaultdict

import numpy as np
from nltk.stem import PorterStemmer
def create_query_vector(term_dict, query_terms):
    stemmer = PorterStemmer()
    query_terms = [stemmer.stem(term.lower()) for term in query_terms]
    query_term_counts = defaultdict(int)
    query_vector = {}
    # Calculate TF for query terms
    for term in query_terms:
        query_term_counts[term] += 1
    for key in query_term_counts.keys():
        query_term_counts[key] = 1 + math.log10(query_term_counts[key])
    # Below calculates TF-IDF for query terms
    for term, count in query_term_counts.items():
        if term in term_dict:
            tf = 1 + math.log10(count)
            idf = term_dict[term][1]
            query_vector[term] = tf * idf

    return query_vector

def create_doc_vectors(term_dict):
    # Calculate TF-IDF vectors for documents
    doc_vectors = defaultdict(lambda: defaultdict(float))
    for term, (_, _, postings) in term_dict.items():
        for doc_id, tf, tf_idf in postings:
            doc_vectors[doc_id][term] = tf_idf
    return doc_vectors

def cosine_similarity(query_vector, doc_vector):
    all_terms = set(query_vector.keys()).union(doc_vector.keys())
    query_array = np.array([query_vector.get(term, 0.0) for term in all_terms])
    doc_array = np.array([doc_vector.get(term, 0.0) for term in all_terms])
    dot_product = np.dot(query_array, doc_array)
    query_norm = np.linalg.norm(query_array)
    doc_norm = np.linalg.norm(doc_array)
    if query_norm == 0 or doc_norm == 0:
        return 0.0
    return dot_product / (query_norm * doc_norm)


def vector_space_model(term_dict, query_terms):
    query_vector = create_query_vector(term_dict, query_terms)
    doc_vectors = create_doc_vectors(term_dict)

    similarities = {}
    for doc_id, doc_vector in doc_vectors.items():
        similarities[doc_id] = cosine_similarity(query_vector, doc_vector)

    # print(f"Query vector: {query_vector}\n")
    # print(f"Document vectors: {doc_vectors}\n")
    print(f"Similarities: {similarities}\n")

    return similarities
