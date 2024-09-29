def solution(array):
    array.sort() #리스트 오름차순 정렬
    L=len(array)
    answer = array[L//2]
    return answer