import cv2
from picamera2 import Picamera2
import time
import numpy as np

# Inicializa o reconhecedor LBPH e carrega o modelo treinado
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

# Carregue o classificador Haar Cascade para detecção
face_cascade = cv2.CascadeClassifier('/home/kaykyRyan/opencv/haarcascade_frontalface_default.xml')

# IDs para nomes (adicione nomes correspondentes aos IDs que você usou)
names = {
    1: "Kayky",
    2: "Pessoa 2",
    # Adicione mais se treinou outras pessoas
}

# Inicializa a câmera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()
time.sleep(2)

while True:
    frame = picam2.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]

        # Reconhece o rosto e retorna o ID e confiança
        id, confidence = recognizer.predict(face_img)

        if confidence < 60:  # limite de confiança, menor é melhor
            nome = names.get(id, "Desconhecido")
            texto = f"{nome} ({round(confidence, 1)})"
        else:
            texto = "Desconhecido"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, texto, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Reconhecimento Facial", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
