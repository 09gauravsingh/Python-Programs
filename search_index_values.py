l = [int(x) for x in input("enter the values of list").split(',')]
element=int(input("enter the element"))
index=0
while index<len(l):
    if l[index]==element:
        print(index,end='')
    index += 1