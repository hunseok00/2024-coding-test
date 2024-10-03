def solution(angle):
    if 90 > angle > 0:
        a=1
    elif angle == 90:
        a=2
    elif 180 > angle > 90:
        a=3
    else:
        a=4
    answer = a
    return answer