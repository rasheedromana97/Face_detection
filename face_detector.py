import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #cvtColor = Covert Color(original image,function to convert to gray img)

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)
# When you set the scaleFactor by 1.05 it means that scale the image by 5% in the next search.
# The minNeighbors tells python how many neighbors to search around the image.
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    #rectangle(img,(start coordinates),(end coordinates),(bgr values),width size)

print(type(faces))
print(faces)

resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
#resize(original image, resolution of the image)
#resolution can be solid numbers like (100,100) but it might stretch out the image so we can access the shape.
#img.shape[width]/3 or any other number, img.shape[height]/3. We must convert to int because we might get float nos.

cv2.imshow("Original Image",img)
cv2.imshow("Resized Image",resized)
cv2.waitKey(0) #0 means when you press any key it will close the window
cv2.destroyAllWindows()
