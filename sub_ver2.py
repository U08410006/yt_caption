# main file of ocr 
import cv2
import easyocr
import sys

f = open('output.txt', 'w') # output file
reader = easyocr.Reader(['ch_tra','en']) # use chinese and english 

x = 0 # x-axis of picture start
y = 580 # y-axis of picture start

w = 1120 # width of pic
h = 150 # height of pic

for i in range(15800): 
 
    path = 'pic/out' + str(i+1) + '.png'
    img = cv2.imread(path)

    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite('output.png', crop_img) # save img to read

    result = reader.readtext('output.png',detail=0)
    l = len(result)

    for j in range(l):
        f.write(result[j])
        f.write(" ")
    f.write('\n')

