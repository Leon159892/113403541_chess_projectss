# -*- coding: utf-8 -*-
"""P1_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XYcmnSHW10p3BxZsO95xhulznA741XCx
"""

a=input().split(" ")
b=input().split(" ")
x1,y1=int(a[0]),int(a[1])
x2,y2=int(b[0]),int(b[1])
position1=checkerboard[x1][y1]
position2=checkerboard[x2][y2]
if (x1==x2 and y1==y2)or(checkerboard[x2][y2]==1):
  print("No")
elif x2==x1+1 and y1==y2:
  print("Yes")
else:
  print("No")