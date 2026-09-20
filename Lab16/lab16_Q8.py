x=int(input("Enter x: "))
y=int(input("Enter y: "))
point=(x,y)
if x>0 and y>0:
    print("Point lies in 1st quadrant")
elif x<0 and y>0:
    print("Point lies in 2nd quadrant")
elif x<0 and y<0:
    print("Point lies in 3rd quadrant")
elif x>0 and y<0:
    print("Point lies in 4th quadrant")
elif x==0 and y!=0:
    print("Point lies on y axis")
elif x!=0 and y==0:
    print("Point lies on x axis")
else:
    print("Point lies on origin")