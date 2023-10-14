import random as r

r.seed(0) # инициализируем позицию псевдорадома в ноль
for i in range (3):
    print (r.random())
r.seed(0)
print()
for i in range (3):
    print (r.random())


a = [2,3,4,6,7,0,2,4]

k=0

for i in range(len(a)):
    if a[i] %2 ==1:
        k+=1
    else:
        a[i-k] = a[i]
    print(i,k,':',a)

a = a[:-k]
print(a)