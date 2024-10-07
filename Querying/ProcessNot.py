def ProcessNot(posting_list, all_doc_ids):
    return all_doc_ids - set(posting_list)