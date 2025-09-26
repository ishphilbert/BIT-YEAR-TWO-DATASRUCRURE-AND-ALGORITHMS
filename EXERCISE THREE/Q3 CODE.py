stack = []
stack.append("A")
stack.append("B")
stack.append("C")
print("Stack now:", stack)

stack.pop()   # remove C
print("After pop:", stack)

stack.append("D")
print("After pushing D:", stack)
print("Top is:", stack[-1])