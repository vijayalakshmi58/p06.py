# p06.py
a1,b1=map(str,input().split())
for i in range(len(a1)):
    if(a1.count(a1[i])==b1.count(b1[i])):
        print("yes")
        break
    else:
        print("no")
         break
