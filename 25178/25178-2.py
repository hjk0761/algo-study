from collections import Counter
#import sys

n = int(input())
a = input()
b = input()
#n = int(sys.stdin.readline())
#a = sys.stdin.readline().strip()
#b = sys.stdin.readline().strip()

s1, s2 = [], []
vowels = ["a", "e", "i", "o", "u"]

for i in a:
  if i not in vowels:
    s1.append(i)
no_vowel_a = ''.join(s1)

for i in b:
  if i not in vowels:
    s2.append(i)
no_vowel_b = ''.join(s2)

if(Counter(a) == Counter(b) and a[0] == b[0] and a[-1] == b[-1]) and no_vowel_a == no_vowel_b:
  print("YES")
else:
  print("NO")