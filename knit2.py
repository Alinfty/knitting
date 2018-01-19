import cv2
from math import sqrt
import numpy as np

img=cv2.imread('c:\\users\\alin\\desktop\\circle.bmp')
kn=cv2.imread('c:\\users\\alin\\desktop\\knit.jpg', 0)

row_i=len(img)
col_i=len(img[0])

row_kn=len(kn)
col_kn=len(kn[0])

for i in range(row_i):
    if i%10==0:
        print(i)
    for j in range(col_i):
        x=row_kn*i//row_i
        y=col_kn*j//col_i
        #img[i][j][0]=int(img[i][j][0])*kn[x][y]//256
        #img[i][j][1]=int(img[i][j][1])*kn[x][y]//256
        #img[i][j][2]=int(img[i][j][2])*kn[x][y]//256
        img[i][j]=[kn[x][y]]*3
cv2.imwrite('c:\\users\\alin\\desktop\\black.bmp', img)