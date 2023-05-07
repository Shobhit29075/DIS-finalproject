import requests
import numpy as np
import matplotlib.pyplot as  plt 
import math
import time
# x = requests.get('http://52.87.235.187/')
c=0
listc=[]
listy=[]
while(c<100):
    c+=1
    #y=requests.get("http://52.66.197.106/").elapsed.total_seconds()
    y=requests.get("http://52.66.197.106/login?user=Nikhil&pwd=nikhil123").elapsed.total_seconds()
    print(y)
    listc.append(c)
    listy.append(y)
    #time.sleep(0.52)
p_arr= np.array(y)
p = np.percentile(p_arr, 99)
print("average", sum(listy)/100)
print("99th percentile", p)
plt.xlabel("count")
plt.ylabel("Latency")
plt.title("52.66.197.106 Mumbai")
plt.plot(listc, listy)
plt.ylim([0,3])
plt.show()
