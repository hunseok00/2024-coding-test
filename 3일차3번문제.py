def solution(array):
    answer = 0
    idx = [0] * 2000
    for i in array:
        idx[i] +=1
    if idx.count(max(idx)) >1:
        return -1
    return idx.index(max(idx))