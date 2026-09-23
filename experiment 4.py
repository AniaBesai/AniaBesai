t = ("a", "b", "c", "d", "e")

print("Tuple:", t)
print("First element:", t[0])
print("Last element:", t[-1])
print("Length:", len(t))
print("Count of b:", t.count("b"))
print("Index of c:", t.index("c"))
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Sum:", sum(t))
print("Is d present?", "d" in t)

l = list(t)
print("Tuple converted to list:", l)

t2 = tuple(l)
print("List converted to tuple:", t2)
