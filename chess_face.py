import cv2

image = cv2.imread("sina.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_detector.detectMultiScale(image_gray, 1.3)
for face in faces:
    x, y, w, h = face
    face_image = image[y:y+h, x:x+w]
    face_image_small = cv2.resize(face_image, [15, 15])
    face_image_big = cv2.resize(
        face_image_small, [w, h], interpolation=cv2.INTER_NEAREST)

    image[y:y+h, x:x+w] = face_image_big


cv2.imshow("result", image)
cv2.waitKey()
