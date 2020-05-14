import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# read the image....
img=cv2.imread('photo1.jpg',1)
# convert the image into gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# to detect the face
faces = face_cascade.detectMultiScale(gray,1.1,4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w , y+h), (255, 0, 0), 3)

# show the output of the image
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()