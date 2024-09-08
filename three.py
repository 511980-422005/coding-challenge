def func1(num):
	srt=str(num)
	for i in range(len(srt)-1):
		if abs(int(srt[i])-int(srt[i+1]))!=1:
			return 0
	return 1

def func2(num1,num2):
	ans=[]
	for num in range(num1,num2+1):
		if func1(num):
			ans.append(num)
	return ans

rg=input("enter range separated by space ")
rg=rg.split(" ")
num1=int(rg[0])
num2=int(rg[1])
ans=func2(num1,num2)

print(ans)
