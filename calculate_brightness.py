import cv2
import imutils
from imutils import paths
import numpy as np

for imagePath in paths.list_images('images'):
	#-----Reading the image-----------------------------------------------------
	img = cv2.imread(imagePath)
	img = imutils.resize(img, width=900)
	img_dot = img

	#-----Converting image to LAB Color model----------------------------------- 
	lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

	#-----Splitting the LAB image to different channels-------------------------
	l, a, b = cv2.split(lab)

	#-----Finding average lightness level in image by fixing some points--------
	y,x,z = img.shape #height, width of image
	print('>> Image Dimension => X:{}, Y:{}'.format(x,y))
	#Now we will decide some dynamic points on image for checking light intensity
	l_blur = cv2.GaussianBlur(l, (11, 11), 5)
	maxval = []
	count_percent = 3 #percent of total image
	count_percent = count_percent/100
	row_percent = int(count_percent*x) #1% of total pixels widthwise
	column_percent = int(count_percent*y) #1% of total pizel height wise
	for i in range(1,x-1):
		if i%row_percent == 0:
			for j in range(1, y-1):
				if j%column_percent == 0:
					pix_cord = (i,j)
					
					cv2.circle(img_dot, (int(i), int(j)), 5, (0, 255, 0), 2)
					img_segment = l_blur[i:i+3, j:j+3]
					(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(img_segment)
					maxval.append(maxVal)

	avg_maxval = round(sum(maxval) / len(maxval))
	print('>> Total points: {}'.format(len(maxval)))
	print('>> Average Brightness: {}'.format(avg_maxval))
	if avg_maxval<50:
		print('>> Image is Dark')
		text = 'Dark'
	else:
		print('>> Image is Bright')
		text = 'Bright'

	cv2.putText(img_dot, "{}".format(text), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

	cv2.imshow('points', img_dot)
	cv2.waitKey(0)
	print()
