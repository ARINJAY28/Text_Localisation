import os
import re
import cv2
import pytesseract
from pytesseract import Output



def main(inputFile):
    outputFile = inputFile.split('.')[0]+'-rect.'+'.'.join(inputFile.split('.')[1:])
    print(outputFile)
    img = cv2.imread(inputFile)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)

    n_boxes = len(d['text'])
    for i in range(n_boxes):
    	if int(d['conf'][i]) > 60:
    			(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    			img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
	
	path = 'Invoice_Images'
	for filename in os.listdir(path):
		main(path+'/'+filename)