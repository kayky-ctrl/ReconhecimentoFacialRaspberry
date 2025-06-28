import cv2
from picamera2 import Picamera2
import time
import os

# Verifica se o classificador foi carregado corretamente
cascade_path = '/home/kaykyRyan/opencv/haarcascade_frontalface_default.xml'
if not os.path.exists(cascade_path):
    print("Erro: classificador Haar não encontrado. Verifique o caminho.")
    exit()

face_cascade = cv2.CascadeClassifier(cascade_path)
if face_cascade.empty():
    print("Erro: falha ao carregar o classificador Haar.")
    exit()

# Inicializa a câmera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()
time.sleep(2)

face_id = input("Digite um ID para sua face: ")
count = 0

while True:
    frame = picam2.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count += 1
        cv2.imwrite(f"faces/face_{face_id}_{count}.jpg", gray[y:y+h, x:x+w])

    cv2.imshow("Captura", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if count >= 30:
        break

cv2.destroyAllWindows()
