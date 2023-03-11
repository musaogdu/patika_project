def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

flatten_list([[1,'a',['cat'],2],[[[3]],'dog'],4,5])


def reverse_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(reverse_list(item))
        else:
            result.append(item)
    return result[::-1]

reverse_list([[1, 2], [3, 4], [5, 6, 7]])
