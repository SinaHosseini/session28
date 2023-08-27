import cv2

image = cv2.imread("input/cats.jpeg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
faces = face_detector.detectMultiScale(image_gray)

counter = 0
for _ in faces:
    counter += 1

print(counter)
