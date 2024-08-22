t = int(input("Enter the Test case: "))
for _ in range(t):
  n = int(input("Enter the element number: "))
  l = []
  for i in range(n):
    a = int(input())
    l.append(a)
  for i in range(len(l)):
    a = 1000
    b = l[i]
    count = 0
    while(0<l[i]):
      if a%10 != b%10:
        count +=1
      a = a//10
      b = b//10 
