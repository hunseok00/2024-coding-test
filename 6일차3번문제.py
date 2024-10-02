def solution(num_list):
    acnt=0
    bcnt=0
    for i in num_list:
        if i%2 == 0:
            acnt+=1
        else:
            bcnt+=1
    answer = [acnt,bcnt]
    return answer