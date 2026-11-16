dim = int(input())
simbolo = "*"

for i in range(dim+1):
    for j in range(i):
        print(simbolo, end = "")
    print()
#     
# 
# for i in range(1,dim+1):
#     print(i*simbolo)

# for i in range(dim,0,-1):
#     print(i*simbolo)
    
# for i in range(1, dim+1):
#     print(" " * (dim-i) + i * simbolo)

# for i in range(dim,0,-1):
#     print(" " * (dim-i) + i * simbolo)

# for i in range(1, dim+1):
#     print(" " * (dim-i) + simbolo * (2*i-1))

# for i in range(1, dim+1, 2):
#     print(" " * ((dim-i)//2) + simbolo * i)
#     
# for i in range(dim,0,-2):
#     print(" " * ((dim-i)//2) + simbolo * i)