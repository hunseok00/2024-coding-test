def solution(numbers):
    a=0
    for i in range(len(numbers)):
        a+=numbers[i]
    answer = a/len(numbers)
    return answer