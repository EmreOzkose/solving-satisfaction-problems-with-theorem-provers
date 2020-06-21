# Ali Yunus Emre Özköse
# BBM405 HW-2
# n-queen input file is generated as below
# dynamic params: 
# 			n: number of queen
# 
# IT IS NOT Z3 WRAPPER. IT IS JUST PREPARING TEXTUAL INPUT FOR Z3 BUILD
# ################## % ################## #

n = 8
print("(and")

print("; at least 1 true in row")
print("(and")
for i in range(1, n + 1):
    temp = "(or"
    for j in range(1, n+1):
        temp += " (p {} {})".format(i, j)
    temp += ")"
    print("\t"+temp)
print(")")

print()

print("; at most 1 true in row")
print("(and")
for i in range(1, n + 1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if j < k:
                print("\t(or (not (p {} {})) (not (p {} {})))".format(i, j, i, k))
print(")")

print()

print("; at least 1 true in col")
print("(and")
for j in range(1, n + 1):
    temp = "(or"
    for i in range(1, n+1):
        temp += " (p {} {})".format(i, j)
    temp += ")"
    print("\t"+temp)
print(")")

print()

print("; at most 1 true in col")
print("(and")
for j in range(1, n + 1):
    for i in range(1, n+1):
        for k in range(1, n+1):
            if j < k:
                print("\t(or (not (p {} {})) (not (p {} {})))".format(i, j, i, k))
print(")")
print()
print("; at most 1 queen at diagonals")
print("(and")
for i in range(1, n + 1):
    for i_ in range(1, n + 1):
        if i < i_:
            for j in range(1, n+1):
                for j_ in range(1, n+1):
                    if i+j == i_+j_ or i-j == i_-j_:
                        print("\t(or (not (p {} {})) (not (p {} {})))".format(i, j, i_, j_))
print(")")
print(")")
