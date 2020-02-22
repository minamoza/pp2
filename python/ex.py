'''
list=[]                 #Ex-1

list+=input()
print(list[0][list[1]])
'''

'''
list=[]                    #Ex-2

list+=input()
for i in range(0,len(list),2):
    print(list[i])
'''

'''
list=[]            #Ex-3

list+=input()
for i in range(list[1],len(list[0])):
    list[0][i]*=list[0][i]
print(list[0])
'''

'''
list=[]            #Ex-4???

list+=input()
list.reverse()
print(list)
'''

'''
list=[]            #Ex-5

list+=input()
for i in range(list[1],len(list[0])):
    del list[0][i]
print(list[0])
'''

'''

list=[]            #Ex-6 XXX

list+=input()
'''

'''
def swapThree(a, b, c):          #7
    a = a + b + c 
    b = a - (b+c)
    c = a - (b+c)
    a = a - (b+c)
    print("a =",a,", b =",b,", c =",c) 

a = 5
b = 3
c = 2
swapThree(a, b, c) 
'''
'''
list=[]                  #8
list+=input()
mx=list[0]
mn=list[0]
for i in range(0,len(list)):
    if list[i]>mx:
        mx=list[i]
    if list[i]<mn:
        mn=list[i]
print(mn,mx)
'''

tuple=()           #9???
tuple+=input()
res=False
for i in range(0,len(tuple)):
     if list in tuple:
        res=True


'''
s1=set()
s2=set()      #10
s3=set()
s1.add(input())
s2.add(input())
s3=s1.difference(s2)
print(s3)
'''