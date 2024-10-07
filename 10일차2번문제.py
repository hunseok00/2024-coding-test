import  numpy as np
def solution(num_list, n):
    num=np.array(num_list)
    num.resize(len(num_list)//n,n)
    return num.tolist()