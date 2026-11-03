import time
def calculate_time(func):
    def wrapper(*args):
        start=time.time()
        result=func(*args)
        end=time.time()
        print("Time taken:",end-start,"seconds")
        return result
    return wrapper

class LinearAlgebra:
    def __init__(self,A,B):
        self.A=A
        self.B=B
    @property
    def A(self):
        return self._A
    @A.setter
    def A(self,value):
        self._A=value
    @property
    def B(self):
        return self._B
    @B.setter
    def B(self, value):
        self._B = value

    @calculate_time
    def multiply(self):
        rows_A=len(self.A)
        cols_A=len(self.A[0])
        rows_B = len(self.B)
        cols_B = len(self.B[0])
        if cols_A!=rows_B:
            raise ValueError("Matrix multiplication not possible")
        result=[]
        for i in range(rows_A):
            row=[]
            for j in range(cols_B):
                total=0
                for k in range(cols_A):
                    total+=self.A[i][k]*self.B[k][j]
                row.append(total)
            result.append(row)
        return result

#Input matrix A
r1=int(input("Rows of A: "))
c1=int(input("Columns of A: "))
A=[]
print("Enter elements of A row by row: ")
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input()))
    A.append(row)

#Input matrix B
r2=int(input("Rows of B: "))
c2=int(input("Columns of B: "))
B=[]
print("Enter elements of B row by row: ")
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input()))
    B.append(row)

obj=LinearAlgebra(A,B)
try:
    result=obj.multiply()
    print("Product matrix: ")
    for row in result:
        print(row)
except ValueError as e:
    print(e)