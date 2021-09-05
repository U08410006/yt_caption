# main file of ocr 
import cv2
import easyocr
import sys

f = open('output_ver3.txt', 'w') # output file
reader = easyocr.Reader(['ch_tra']) # use chinese 

x = 0 # x-axis of picture start
y = 580 # y-axis of picture start

w = 1120 # width of pic
h = 150 # height of pic

for i in range(15710): 
    
    path = 'pic/out' + str(i+1) + '.png'

    try:
        img = cv2.imread(path)
    except:
        break

    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite('output.png', crop_img) # save img to read

    result = reader.readtext('output.png')
    l = len(result)

    for j in range(l):
        if((abs(result[j][0][0][1] - 8) <= 8) or (abs(result[j][0][0][1] - 37) <= 8) or (abs(result[j][0][0][1] - 28) <= 8 )):
            f.write(result[j][1])
            f.write(" ")
        elif (abs(result[j][0][0][1] - 56) <= 8):
            f.write("&")
            f.write(result[j][1])
            f.write(" ")
        else:
            f.write("#")
            f.write(result[j][1])
            f.write(" ")
    f.write('\n')

