import cv2

# read the image file and Python sees it as a numpy array
img=cv2.imread("galaxy.jpg",0)

print(type(img))
print(len(img))
print(img)
print(img.shape)
print(img.ndim)

# resized_image=cv2.resize(img,(500,1000)) # on this line, you can put in exact values for resizing the image.
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

# show image on screen
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("Galaxy_resized_bw.jpg",resized_image)
cv2.waitKey(0) # here if the argument is '0', then the program waits for a user to press any key to close the window. If there is a value, it is calculated in miliseconds. E.G an argument of '2000' is 2000 miliseconds or 2 seconds before the window will close.
cv2.destroyAllWindows()
