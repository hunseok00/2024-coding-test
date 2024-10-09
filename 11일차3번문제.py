def solution(numbers):
    numbers.sort()
    l=len(numbers)
    answer = numbers[l-1]*numbers[l-2]
    return answer