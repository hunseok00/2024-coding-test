def solution(slice, n):
    if n%slice >=1:
        answer=n//slice+1
    else:
        answer=n//slice
    return answer