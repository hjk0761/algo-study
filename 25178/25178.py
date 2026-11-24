from collections import Counter

n = int(input())
a = input()
b = input()

s1, s2 = [], []
s11, s22 = [], []
vowels = ["a", "e", "i", "o", "u"]

for i in range(n):
    s1.append(a[i])
    s2.append(b[i])
    
if Counter(s1) == Counter(s2) and s1[0] == s2[0] and s1[n-1] == s2[n-1]:
  for i in range(len(s1)):
    if s1[i] in vowels:
      continue
    else: 
      s11.append(s1[i])
  for i in range(len(s2)):
    if s2[i] in vowels:
      continue
    else:
      s22.append(s2[i])

  if s11 == s22:
    print("YES")
  else: 
    print("NO")
else:
  print("NO")
