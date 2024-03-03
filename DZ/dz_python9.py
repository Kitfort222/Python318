s1 = "test"
s2 = "string"
a = set(s1) | set(s2)
print(a)
for i in a:
    print(i, end=" ")