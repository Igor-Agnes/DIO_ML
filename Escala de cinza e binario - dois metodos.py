####escala de cinza matplot
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('test.jpg')

R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray, cmap='gray')
plt.show()


########Binario openVC
import cv2 
img = cv2.imread(test.jpg', 2) 
  
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
  
cv2.imshow("Binary", bw_img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 