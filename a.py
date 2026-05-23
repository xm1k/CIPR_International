s = {}
with open("access.log") as file:
    for line in file:
        a = line.rstrip()
        g = a.split()[0]
        s[g] = s.get(g, 0) + 1
print(s)
