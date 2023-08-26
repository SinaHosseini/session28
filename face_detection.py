import cv2

image = cv2.imread("sina.jpg ")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_sticker = cv2.imread("")

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_detector.detectMultiScale(image_gray, 1.3)

for face in faces:
    x, y, w, h = face
    cv2.rectangle(image_gray, [x, y], [x+w, y+h], 0, 6)

cv2.imshow("result", image_gray)
cv2.waitKey()
