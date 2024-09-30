import math
def solution(n):
    c=0
    while True:
        c+=1
        if c%n==0 and c%6==0:
            break
    answer = c//6
    return answer