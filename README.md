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
##### Step 1: calculate_brightness.py
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

Hope you enjoyed today's tutorial. Don't forget to star the repository.
if you have any query, feel free to ask.
Join me here at ``insta/the.nitin.rai``
Connect me at ``mneonizer@gmail.com``
