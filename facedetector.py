import cv2
face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
""""
img=cv2.imread('Iron-Man.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_coordinates=face_data.detectMultiScale(gray)
print(face_coordinates)
for x,y,w,h in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("gray",img)
cv2.waitKey()
"""
frame=cv2.VideoCapture(0)
while True:
    ret,vid=frame.read()
    gray1=cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)
    face_coordinates=face_data.detectMultiScale(gray1)
    for x,y,w,h in face_coordinates:
        cv2.rectangle(vid,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('framee',vid)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

print("code completed")
