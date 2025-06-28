import cv2
import numpy as np
import os

# Caminho onde as imagens foram salvas
path = 'faces'

# Criar reconhecedor LBPH
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Carregar classificador Haar para validar rostos (opcional, mas recomendado)
face_cascade = cv2.CascadeClassifier('/home/kaykyRyan/opencv/haarcascade_frontalface_default.xml')

def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []

    for image_path in image_paths:
        # Carrega imagem em escala de cinza
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        # Extrair ID do nome do arquivo, ex: face_1_10.jpg -> id=1
        id = int(os.path.split(image_path)[-1].split('_')[1])

        faces = face_cascade.detectMultiScale(img)

        for (x, y, w, h) in faces:
            face_samples.append(img[y:y+h, x:x+w])
            ids.append(id)

    return face_samples, ids

print("Treinando o modelo...")

faces, ids = get_images_and_labels(path)
recognizer.train(faces, np.array(ids))

# Salvar modelo treinado
recognizer.write('trainer.yml')

print(f"Treinamento concluído com {len(np.unique(ids))} pessoas.")

