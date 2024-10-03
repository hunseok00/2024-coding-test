def solution(n, k):
    if n//10>0:
        k=k-n//10
        
    t=n*12000+k*2000
    answer = t
    return answer