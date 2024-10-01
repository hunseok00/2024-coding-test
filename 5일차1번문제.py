def solution(price):
    if price < 100000:
        p=price
    elif 100000 <= price and price <300000:
        p=price*95//100
    elif 300000<= price and price <500000:
        p=price*90//100
    else:
        p=price*80//100
    answer = p
    return answer