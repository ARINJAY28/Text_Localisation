import os,sys
import numpy as np
import cv2
import pytesseract
import spacy
import re


def text_detect(img,ele_size=(8,2)): #
    if len(img.shape)==3:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_sobel = cv2.Sobel(img,cv2.CV_8U,1,0)#same as default,None,3,1,0,cv2.BORDER_DEFAULT)
    img_threshold = cv2.threshold(img_sobel,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)
    element = cv2.getStructuringElement(cv2.MORPH_RECT,ele_size)
    img_threshold = cv2.morphologyEx(img_threshold[1],cv2.MORPH_CLOSE,element)
    res = cv2.findContours(img_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if cv2.__version__.split(".")[0] == '3':
        _, contours, hierarchy = res
    else:
        contours, hierarchy = res
    Rect = [cv2.boundingRect(i) for i in contours if i.shape[0]>100]
    RectP = [(int(i[0]-i[2]*0.08),int(i[1]-i[3]*0.08),int(i[0]+i[2]*1.1),int(i[1]+i[3]*1.1)) for i in Rect]
    return RectP


def main(inputFile):
    outputFile = inputFile.split('.')[0]+'-rect.'+'.'.join(inputFile.split('.')[1:])
    print(outputFile)
    img = cv2.imread(inputFile)

    print(pytesseract.image_to_string(img))

    rect = text_detect(img)
    ROI_number = 0
    Data = []
    for i in reversed(rect):
        cv2.rectangle(img,i[:2],i[2:], (0, 255, 0), 2)
        ROI = img[i[1]:i[3], i[0]:i[2]]
        ROI_number += 1
        filename = 'ROI_' + str(ROI_number) + '.png'

    cv2.imshow("Sample",img)
    cv2.waitKey(0)
    print("===============================================================================================================================================================================================")

if __name__ == '__main__':
	
	path = 'Invoice_Images'
	for filename in os.listdir(path):
		main(path+'/'+filename)


