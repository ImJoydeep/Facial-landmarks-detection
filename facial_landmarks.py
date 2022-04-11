from unittest import result
import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

image = cv2.imread('girl.png')
height, width, _ = image.shape
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result = face_mesh.process(rgb_image)
for facial_landmarks in result.multi_face_landmarks:
    for i in range(0, 468):
        pt1 = facial_landmarks.landmark[i]
        x = int(pt1.x * width)
        y = int(pt1.y * height)

        # Syntax: cv2.circle(image, center_coordinates, radius, color, thickness)
        cv2.circle(image,(x,y),1,(255,0,0),2)

cv2.imshow("frame", image)
cv2.waitKey(0)