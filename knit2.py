import cv2
from math import sqrt
import numpy as np


kn=cv2.imread('knit.jpg', 0)


m=8
r=3*m//2

knit=[[ kn[1725+(135*i)//r][710+(120*j)//r]+6 for j in range(r)] for i in range(r)]\
+[[ kn[1860+(80*i)//m][710+(120*j)//r]+6 for j in range(r)] for i in range(m)]\
+[[ kn[1940+(135*i)//r][710+(120*j)//r]+6 for j in range(r)] for i in range(r)]


cv2.imwrite('c:\\users\\alin\\desktop\\temp.bmp', np.array(knit))
print(knit)

ma=0
mi=300
for a in knit:
    for b in a:
        if b>ma:
            ma=b
        if b<mi:
            mi=b

print(ma, mi)
img=cv2.imread('c:\\users\\alin\\desktop\\20160809_091229.jpg')

row=len(img)
col=len(img[0])

#newimg=[[[int(img[i][j][0])*int(img[i][j][0])/(256.0*256),int(img[i][j][1])*int(img[i][j][1]/(256.0*256)),int(img[i][j][2])*int(img[i][j][2])/(256.0*256)] for j in range(col)] for i in range(row)]
newimg=np.float32(img)
newimg=newimg*1/256
#newimg=newimg*newimg


for i in range(-1,row//(r+m)+1):
    print(i)
    for j in range(-1,col//r+1):
        sum=[0,0,0]
        s=0
        colorlst=[]
        if j%2==0:
            for k in range(r):
                for l in range(k+1):
                    if 0<=(r+m)*i+k<row and 0<=r*j+l<col:
                        s+=1
                        colorlst.append(list(newimg[(r+m)*i+k][r*j+l]))
            for k in range(m):
                for l in range(r):
                    if 0<=(r+m)*i+r+k<row and 0<=r*j+l<col:
                        s+=1
                        colorlst.append(list(newimg[(r+m)*i+r+k][r*j+l]))
                        
            for k in range(r):
                for l in range(r-k):
                    if 0<=(r+m)*i+m+r+k<row and 0<=r*j+r-l-1<col:
                        s+=1
                        colorlst.append(list(newimg[(r+m)*i+m+r+k][r*j+r-l-1]))
            
            if s!=0:
                sorted(colorlst)
                avg=colorlst[s//2]

                for k in range(r):
                    for l in range(k+1):
                        if 0<=(r+m)*i+k<row and 0<=r*j+l<col:
                            img[(r+m)*i+k][r*j+l]= list(map(lambda x: int(x*knit[k][l]), avg))
                for k in range(m):
                    for l in range(r):
                        if 0<=(r+m)*i+r+k<row and 0<=r*j+l<col:
                            img[(r+m)*i+r+k][r*j+l]= list(map(lambda x: int(x*knit[r+k][l]), avg))
                for k in range(r):
                    for l in range(r-k):
                        if 0<=(r+m)*i+m+r+k<row and 0<=r*j+r-l-1<col:
                            img[(r+m)*i+m+r+k][r*j+r-l-1]= list(map(lambda x: int(x*knit[r+m+k][r-l-1]), avg))

        else:
            for k in range(r):
                for l in range(k+1):
                    if 0<=(r+m)*i+k<row and 0<=r*j+r-l-1<col:
                        s+=1
                        colorlst.append(list(newimg[(r+m)*i+k][r*j+r-l-1]))
            for k in range(m):
                for l in range(r):
                    if 0<=(r+m)*i+r+k<row and 0<=r*j+l<col:
                        s+=1
                        colorlst.append(list(newimg[(r+m)*i+r+k][r*j+l]))
            for k in range(r):
                for l in range(r-k):
                    if 0<=(r+m)*i+m+r+k<row and 0<=r*j+l<col:
                        s+=1
                        colorlst.append(list(newimg[(r+m)*i+m+r+k][r*j+l]))

            if s!=0:
                avg=sorted(colorlst)[s//2]
       
                for k in range(r):
                    for l in range(k+1):
                        if 0<=(r+m)*i+k<row and 0<=r*j+r-l-1<col:
                            img[(r+m)*i+k][r*j+r-l-1]= list(map(lambda x: int(x*knit[k][l]), avg))
                for k in range(m):
                    for l in range(r):
                        if 0<=(r+m)*i+r+k<row and 0<=r*j+l<col:
                            img[(r+m)*i+r+k][r*j+l]= list(map(lambda x: int(x*knit[r+k][r-l-1]), avg))
                for k in range(r):
                    for l in range(r-k):
                        if 0<=(r+m)*i+m+r+k<row and 0<=r*j+l<col:
                            img[(r+m)*i+m+r+k][r*j+l]= list(map(lambda x: int(x*knit[r+m+k][r-l-1]), avg))

cv2.imwrite('c:\\users\\alin\\desktop\\re20160809_091229_2.jpg', img)