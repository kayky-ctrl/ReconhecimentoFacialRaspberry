# ReconhecimentoFacialRaspberry
Sistema de reconhecimento facial em Python para Raspberry Pi. Funcionalidades: 1) Captura de rostos 2) Treinamento do modelo LBPH 3) Identificação em tempo real. Usa OpenCV e Picamera2. Perfeito para controle de acesso, segurança e projetos IoT. Requer módulo de câmera.

# **Sistema de Reconhecimento Facial - Raspberry Pi**  

![OpenCV](https://img.shields.io/badge/OpenCV-5.0%2B-green)  
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)  
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Compatible-red)  

Um sistema completo de reconhecimento facial desenvolvido para Raspberry Pi, utilizando **OpenCV** e **Picamera2**.

---

## **📌 Funcionalidades**  
✔ **Cadastro de rostos** - Captura e armazena imagens faciais  
✔ **Treinamento do modelo** - Usa algoritmo LBPH do OpenCV  
✔ **Reconhecimento em tempo real** - Identifica pessoas com confiança  

---

## **🛠 Tecnologias**  
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)  
- ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)  
- ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=flat-square&logo=raspberry-pi&logoColor=white)  

---

## **🚀 Como Usar**  

### **1. Pré-requisitos**  
```bash
sudo apt update
sudo apt install python3-opencv python3-pip
pip install picamera2 numpy
```

### **2. Estrutura do Projeto**
📂 projeto/

├── 📂 faces/               # Armazena imagens capturadas

├── 📜 ReconhecimentoFacialRegistrarFace.py   # Captura rostos

├── 📜 TreinamentoReconhecimentoFacial.py     # Treina modelo

└── 📜 ReconhecimentoFinalFace.py             # Reconhecimento

### **3. Execução**
🔹 Cadastrar rostos:

python3 ReconhecimentoFacialRegistrarFace.py
🔹 Treinar modelo:

python3 TreinamentoReconhecimentoFacial.py
🔹 Reconhecimento:

python3 ReconhecimentoFinalFace.py
⚙ Personalização
Adicionar pessoas: Execute o script de captura com novo ID

Ajustar sensibilidade: Modifique o limiar em ReconhecimentoFinalFace.py

## **🔧 Solução de Problemas**
Erro no classificador Haar Cascade:

sudo apt install opencv-data
Verifique o caminho:
/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml

### **📜 Licença**
MIT © kayky-ctrl

### **⭐ Dúvidas? Abra uma issue!**
