import math
def solution(numer1, denom1, numer2, denom2):
    numer= denom1*numer2+denom2*numer1
    denom=denom1*denom2
    gcd= math.gcd(denom, numer) #최대공약수를 구한다
    answer=[numer//gcd,denom//gcd]
    return answer