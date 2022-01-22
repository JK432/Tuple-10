#Create a tuple with 20 numbers. Write a python program to print another tuple whose values are even numbers from the first tuple
tup=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
i=0
tup2=[]

for x in tup:
  if(x%2==0):
    tup2.append(x)
    i=i+1

tup2=tuple(tup2)
print(tup2)
 