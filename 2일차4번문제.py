def solution(numbers):
    answer=[] #answer을 수열로 정의
    for i in numbers: #주어진 수열 전체 내에서 반복
        answer.append(i*2) #새로운 수열에 주어진 수열의 원소*2를 추가
    return answer