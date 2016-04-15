s = input()
ss = {}
m = 0
for i in range(len(s)):
    c = 0
    l  = s[i]
    while i+1 < len(s) and s[i] <= s[i+1]:
        c += 1
        i += 1
        l += s[i]
    ss[c] = ss.get(c, l)
    m = max(ss.keys())

print(s.count(ss[m]))