import cv2
import pytesseract
image = cv2.imread('test01.jpg')
img_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb,lang='eng'))
cv2.waitKey(0)