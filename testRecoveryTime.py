import requests
import time

flag=0
while(1):
    y=requests.get("http://www.lb.shobhitsingh.com/login?user=Shobhit&pwd=shobhit123").text
    print(y)
    if y!="<h1>Welcome Shobhit</h1>" and flag==0:
        t1=time.time()
        flag=1
    elif y=="<h1>Welcome Shobhit</h1>" and flag==1:
        t2=time.time()
        break
print("Recovery Time:",t2-t1)

