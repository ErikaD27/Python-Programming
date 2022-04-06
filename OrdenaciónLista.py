
lis=[4,8,3,2,7]
print("lista inicial:",lis)
for i in range(1,len(lis)):
    lis2=lis[i]
    j=i-1
    while j>=0 and lis[j]>lis2:
        lis[j+1]=lis[j]
        j=j-1
    lis[j+1]=lis2
print('Lista',lis)




