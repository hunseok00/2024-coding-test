def solution(my_string):
    removes= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    removel=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in removes:
        my_string = my_string.replace(i, "")
    for i in removel:
        my_string = my_string.replace(i, "")
    my_string= list(my_string)
    cnt=0
    for i in my_string:
        cnt=cnt+int(i)
    return cnt