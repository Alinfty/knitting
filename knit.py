import cv2

img=cv2.imread('c:\\users\\alin\\desktop\\circle.bmp')

r = 20
row=len(img)
col=len(img[0])
s=r*(r-1)+r*r
for i in range(row//(2*r)-1):
    print(i)
    for j in range(col//r-1):
        sum=[0,0,0]
        if j//2==0:
            for k in range(r):
                for l in range(k):
                    sum[0]+=img[2*r*i+k][r*j+l][0]
                    sum[1]+=img[2*r*i+k][r*j+l][1]
                    sum[2]+=img[2*r*i+k][r*j+l][2]
            for k in range(r):
                for l in range(r):
                    sum[0]+=img[2*r*i+r+k][r*j+l][0]
                    sum[1]+=img[2*r*i+r+k][r*j+l][1]
                    sum[2]+=img[2*r*i+r+k][r*j+l][2]
            for k in range(r):
                for l in range(r):
                    sum[0]+=img[2*r*i+2*r+k][r*j+r-l][0]
                    sum[1]+=img[2*r*i+2*r+k][r*j+r-l][1]
                    sum[2]+=img[2*r*i+2*r+k][r*j+r-l][2]
        else:
            for k in range(r):
                for l in range(k):
                    sum[0]+=img[2*r*i+k][r*j+r-l][0]
                    sum[1]+=img[2*r*i+k][r*j+r-l][1]
                    sum[2]+=img[2*r*i+k][r*j+r-l][2]
            for k in range(r):
                for l in range(r):
                    sum[0]+=img[2*r*i+r+k][r*j+l][0]
                    sum[1]+=img[2*r*i+r+k][r*j+l][1]
                    sum[2]+=img[2*r*i+r+k][r*j+l][2]
            for k in range(r):
                for l in range(r):
                    sum[0]+=img[2*r*i+2*r+k][r*j+l][0]
                    sum[1]+=img[2*r*i+2*r+k][r*j+l][1]
                    sum[2]+=img[2*r*i+2*r+k][r*j+l][2]
        sum[0]=sum[0]/s
        sum[1]=sum[1]/s
        sum[2]=sum[2]/s

        if j//2==0:
            for k in range(r):
                for l in range(k):
                    img[2*r*i+k][r*j+l][0]=sum[0]
                    img[2*r*i+k][r*j+l][1]=sum[1]
                    img[2*r*i+k][r*j+l][2]=sum[2]
            for k in range(r):
                for l in range(r):
                    img[2*r*i+r+k][r*j+l][0]=sum[0]
                    img[2*r*i+r+k][r*j+l][1]=sum[1]
                    img[2*r*i+r+k][r*j+l][2]=sum[2]
            for k in range(r):
                for l in range(r):
                    img[2*r*i+2*r+k][r*j+r-l][0]=sum[0]
                    img[2*r*i+2*r+k][r*j+r-l][1]=sum[1]
                    img[2*r*i+2*r+k][r*j+r-l][2]=sum[2]
        else:
            for k in range(r):
                for l in range(k):
                    img[2*r*i+k][r*j+r-l][0]=sum[0]
                    img[2*r*i+k][r*j+r-l][1]=sum[1]
                    img[2*r*i+k][r*j+r-l][2]=sum[2]
            for k in range(r):
                for l in range(r):
                    img[2*r*i+r+k][r*j+l][0]=sum[0]
                    img[2*r*i+r+k][r*j+l][1]=sum[1]
                    img[2*r*i+r+k][r*j+l][2]=sum[2]
            for k in range(r):
                for l in range(r):
                    img[2*r*i+2*r+k][r*j+l][0]=sum[0]
                    img[2*r*i+2*r+k][r*j+l][1]=sum[1]
                    img[2*r*i+2*r+k][r*j+l][2]=sum[2]

cv2.imwrite('c:\\users\\alin\\desktop\\re.bmp', img)