li = ['XYZ', 'ADR', 'PKL', 'APK', 'YUJ', 'KOMM', 'QWU', 'LKK', 'RES', 'THU']
s = input()
s1 = s.split(' ')
for c in s1:
    if c in li:
        tmp = s1.index(c)
        s1.pop(tmp)
        s1.insert(tmp,"#" * len(c))
        print(s1)
s2 = " "
s2 = s2.join(s1)
print(s2)
