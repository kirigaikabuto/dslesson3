# #abbcddef
# #b
# #2
# count = count +1
s = "abbcddef"
find = "b"
counter=0
for i in range(len(s)):
    if s[i] == find:
        counter = counter +1
#i=0 s[i]='a' counter=0
#i=1 s[i]='b' counter=0+1=1
#i=2 s[i]='b' counter=1+1 =2
#i=3 s[i]='c' counter=2
print(f"{find} count={counter}")
