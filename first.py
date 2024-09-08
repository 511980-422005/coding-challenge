num=int(input("enter value of N: "))
size_of_lst=(num*2+2)
lst1=input(f"enter {size_of_lst} values separated by space ")
lst1=[int(x) for x in lst1.split()]

def function(list2):
    result=[]
    for x in set(list2):
        if list2.count(x)==1:
            result.append(x)
    return sorted(result)
print(function(lst1))
