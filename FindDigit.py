x=[0,"b",2,3,"pencil",5,6,"notebook",8,"cb",10, 13, "rte"]
y=[i for i in x if str(i).isdigit()]
print(y)
# [0, 2, 3, 5, 6, 8, 10, 13]