def solution(my_string, n):
    c=[]
    for i in range(len(my_string)):
        c.append(my_string[i]*n)
    answer = "".join(c)
    return answer