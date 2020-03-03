# using slicing
l = [1, 2, 3, 4, 5, 6]

a = l[0]  # 1
b = l[1:]  # [2, 3, 4, 5, 6]
print(a)
print(b)

# using unpacking
c, d = l[0], l[1:]
print(c)  # 1
print(d)  # [2, 3, 4, 5, 6]


# using * operator
e, *f = l
print(e)  # 1
print(f)  # [2, 3, 4, 5, 6]


l = [1, 2, [3, 4]]
g, h, (i, j) = l

print(g) # 1
print(h) # 2
print(i) # 3
print(j) # 4

k, *l, (m, *n) = [1, 2, 3, 'python']
print(k) # 1
print(l) # [2, 3]
print(m) # p
print(n) # ['y', 't', 'h', 'o', 'n']
