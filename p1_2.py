# -*- coding: utf-8 -*-
"""P1_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bmGWgCW45mt0IuEOjij3hFnIHSQroWrG
"""

a=input().split(" ")
b=input().split(" ")
x1,y1=int(a[0]),int(a[1])
x2,y2=int(b[0]),int(b[1])
position1=checkerboard[x1][y1]
position2=checkerboard[x2][y2]
if (x1==x2 and y1==y2)or(checkerboard[x2][y2]==1):
  print("No")
elif x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
    clear = True
    dx = (x2 - x1 > 0) - (x2 - x1 < 0)
    dy = (y2 - y1 > 0) - (y2 - y1 < 0)

    cx = x1 + dx
    cy = y1 + dy
    while cx != x2 or cy != y2:
        if checkerboard[cx][cy] == 1:
            clear = False
            break
        cx += dx
        cy += dy

    if clear:
        print("Yes")
    else:
        print("No")
else:
    print("No")