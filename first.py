# Write your code here :-)
a = ["boy", "girl", "tunji", "him"]
for i in range(-len(a),0):
    if i != -1:
        print(a[i], end = ", ")
    else:
        print(f"and {a[i]}.", end = "\n")
