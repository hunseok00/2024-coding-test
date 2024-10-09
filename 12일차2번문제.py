def solution(my_string):
    remove= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in remove:
        my_string = my_string.replace(i, "")
    my_string= list(my_string)
    my_string.sort()
    lst=[]
    for i in my_string:
        lst.append(int(i))
    return lst