num=input()
def pow(x,y):
    result=x**y
    return result
sum=0
for n in range(len(num)):
    p=pow(int(num[n]),len(num))
    sum+=p
if sum==int(num):
    print(True)
else:
    print(False)
