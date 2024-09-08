num=int(input("enter num"))
str=input("enter string")
dict=input("enter dict seperated by space ").split()
def function(str,dict):
    while str:
        find=False
        for word in dict:
            if str[:len(word)]==word:
                str=str[len(word):]
                find=True
                break
        if not find:
            return 0
    return 1
print(function(str,dict))
