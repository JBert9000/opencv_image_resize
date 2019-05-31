import cv2
import glob
import os
# from datetime import datetime

# This program works, but I didn't want to put my entire PATH in this repo since it will be public.
os.chdir("\\opencv_image_resize\\images")
images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,1)
    resized_img=cv2.resize(img,(500,500))
    img=cv2.imwrite("resized_"+image,resized_img)

# Below are my other attempts of figuring this out.

# for image_file in os.listdir('\\opencv_image_resize\\images'):
#     if image_file.endswith(".jpg"):
#         now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
#
#         img=cv2.imread('\\opencv_image_resize\\images'+image_file)
#         new_width = 500
#         new_height = 500
#         img=cv2.resize(img, (new_width,new_height))
#         img=cv2.imwrite('\\opencv_image_resize\\images'+now+'.jpg')



# path='/opencv_image_resize/images/'
#
# img=cv2.resize(path,[500],[500])
# read=cv2.imread(img)
#
# print(read)



# img=cv2.imread("galaxy.jpg")
# images=cv2.imread(["news.jpg","photo.jpg"])
# print(images)

# print(img)
#
# resize=cv2.resize(img(500,500))
#
# cv2.imshow(img,resize)
# cv2.waitKey(0)
