# Text_Localisation
Using OpenCV and PyTesseract to localose text in scanned images such as invoice, reciepts, agreements
# Usage
Create a folder in Root_Directory to store test images<\br>
Then, in command line execute the following commands, based on requirement<\br>
- python3 Text_Localisation-OpenCV.py
- python3 Text_Localisation-PyTesseract.py
# Results
PyTesseract performs better in scanned images when compared to opencv
# Bounding_Boxes
When running **Text_Localisation-OpenCV.py**,change the element size in text_detect function to get a different sized bounding boxes. Smaller ele_size corresponds to more accurate detection(like letters)
