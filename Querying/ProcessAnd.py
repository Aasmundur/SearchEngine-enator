from Querying.Intersect import intersect


def ProcessAnd(posting_lists):
    if not posting_lists:
        return set()
    result = posting_lists[0]
    for posting_list in posting_lists[1:]:
        result = result.intersection(posting_list)
    return result