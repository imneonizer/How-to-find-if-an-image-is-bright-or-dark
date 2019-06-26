# How-to-find-if-an-image-is-bright-or-dark
#### Idea 
Certain regions of images will be selected to pickup the brightness level and finally averaging those value will give the average brightness level of the image.

>Finally after getting a average brightness level balue we can decide threshold
>below which images will be considered as dark
>one more interesting this is, the code is highly dynamic
>meaning we can modify it to pick only certain percent of points from the image
>for finding averagae brightness values.
>No matter whether the image size is 100X100 pixels or 1000X1000 pixels
>the program is unaffacted by image size.


## External Modules required
```
>> pip install opencv-contrib-python
>> pip install numpy
>> pip install imutils
```
### lets move to the Practical hands on
##### Step 1: Run calculate_brightness.py
You will see output something similar to this
![output](https://github.com/imneonizer/How-to-find-if-an-image-is-bright-or-dark/blob/master/assets/1.jpg)
##### Step 2: Lets try a different image
Simply press esc Key to test on another image that i have provided
![Next image](https://github.com/imneonizer/How-to-find-if-an-image-is-bright-or-dark/blob/master/assets/2.jpg)

>BTW you can place your own images inside the images directory or
>modify the code a little bit to input your own images
>just remove the Parent For loop from line 6
>and change line 8 ``img = cv2.imread(imagePath)`` to ``img = cv2.imread('images/1.png')``

### Actual image High Resolution
![Original image](https://github.com/imneonizer/How-to-find-if-an-image-is-bright-or-dark/blob/master/images/high_size_colored_bright.jpg)

### Actual image Low Resolution
![Original image](https://github.com/imneonizer/How-to-find-if-an-image-is-bright-or-dark/blob/master/images/low_size_dark.jpg)

### Here is the little code snippet
>to help you understand whats going on behind the scenes
```
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
```
>firstly we are converting the image into L*A*B color spaces
>did a slight Gaussian Blurring to cancel out the Noises.
>then splitting it to extract the ``L`` Channel which is responsible for the brightness levels
>after which we calculate number of points we are going to check
>rowise and column wise
>in our case we are taking every 1% pizel out of total pizels
>and finally we detect brightness level at that point
>in the end we just average out all the values

Hope you enjoyed today's tutorial. Don't forget to star the repository.
if you have any query, feel free to ask.
Join me here at ``insta/the.nitin.rai``
Connect me at ``mneonizer@gmail.com``
