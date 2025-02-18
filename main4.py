#!/usr/bin/python
import cv2
import numpy as np
import zmq
import base64

#Iniciar ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://10.2.20.3:5555")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error")

# Bucle principal
while True:
    ret, frame_rgb = cap.read()
    if not ret:
        print("No es pot llegir el frame RGB")
        break

    # Mostrar la imatge
    cv2.imshow("Color Image", frame_rgb)
    _, buffer = cv2.imencode('.jpg', frame_rgb)
    socket.send(buffer)
    key = cv2.waitKey(1) & 0xFF

    # Si es prem la tecla 'c', sortir del bucle
    if key == ord("c"):
        break

# Tancar totes les finestres i alliberar el dispositiu de profunditat
cap.release()
cv2.destroyAllWindows()
