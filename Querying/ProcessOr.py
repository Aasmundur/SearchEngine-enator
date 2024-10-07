from Querying.Union import union


def ProcessOr(posting_lists):
    if not posting_lists:
        return set()
    result = set(posting_lists[0])
    for posting_list in posting_lists[1:]:
        result = set(union(list(result), list(posting_list)))
    return result