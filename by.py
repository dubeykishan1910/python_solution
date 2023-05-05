# a=[100,50,30,20,10]
# amount=290
# co=0
# new_amount=0
# for i in range(len(a)):
#     while(True):
#         if a[i]<=amount:
#             new_amount+=a[i]
#             amount-=a[i]
#             co+=1
#         else:
#             break

# print(co)
# print(new_amount)
# print(amount) 




#binary search
# a=[11,1,99,7,30,8,0]

# l=0
# r=len(a)-1
# mid=l+(r+l)//2

# search=84
# aa=True
# while(l<=r):
#     mid =l+(r-l)//2

#     if a[mid]==search:
#         print("at index ",mid)
#         aa=False
#         break
#     elif a[mid]<search:
#         l=mid+1
#     elif a[mid]>search:
#         r=mid-1

# if aa:
#     print("element not in aray")
    

# import sys
# minn=sys.maxsize   
# st="aagbbc"
# o="ancdef"
# a={}


# for i in range(6):
#     if (st[i] not in a):
#         a[st[i]]=i
#         print(a)

# for i in range(6):
#     if (o[i] in a and a[o[i]] < minn):
#         minn=a[o[i]]
#         print(minn)



# print(a)




s1=input()
s2=input()
c=0
s1=[i for i in s1]
s2=[i for i in s2]

while(1):
  if s1==s2:
    print(c)
    break
  else:
    s1.insert(0,s1.pop())
    c=c+1


