
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


