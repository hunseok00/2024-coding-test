def solution(n):
    x=0
    a=[]
    while x <=n:
        if x%2 == 0:
            a.append(x)
        x+=1
    return sum(a)