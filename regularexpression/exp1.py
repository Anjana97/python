import re
matcher=re.finditer("ab","abababaab")
cnt=0
for match in matcher:
    #print(match.group())
    print(match.start())
    cnt+=1
print("count",cnt)
