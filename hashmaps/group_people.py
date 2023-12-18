from collections import defaultdict


def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    groups = defaultdict(list)
    res = []

    for index, size in enumerate(groupSizes):
        # here we append the index to the specific size key value which is set as size
        groups[size].append(index)
        # once a size key has its own length in values appended we pop the specific size
        # and append it to the res list
        if len(groups[size]) == size:
            res.append(groups.pop(size))
    return res
