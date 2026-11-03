n=int(input("Enter a number:"))
print("  ".rjust(5),end="")
for row in range(1,n+1):
    print(f"{row:5}",end="")
print()
for row in range(1,n+1):
    print(f"{row:5}",end="")
    for column in range(1,n+1):
        print(f"{row*column:5}",end="")
    print()