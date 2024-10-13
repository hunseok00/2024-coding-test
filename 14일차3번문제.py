def solution(cipher, code):
    b=[]
    a=len(cipher)//code
    for i in range(a):
        b.append(cipher[i*code+code-1])
    answer = b
    return ''.join(answer)