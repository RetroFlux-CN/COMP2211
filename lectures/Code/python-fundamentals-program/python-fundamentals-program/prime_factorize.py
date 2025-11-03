# File: prime_factorize.py

def prime_check(n):
  for i in range(2,n):
    if n%i == 0: return False
  return True

n = int(input("Enter the Number: "))
print(str(n)+" = ",end='')

for i in range (2,n+1):
  c = 0
  if prime_check(i) == True:
    while True:
      if(n%i == 0):
        n /= i
        c+= 1
      else: break
    if c == 1:
      print(str(i)+" x ",end='')
    elif c !=0:
      print(str(i)+"^"+str(c)+" x ",end='')

print(" \b\b\b ")

