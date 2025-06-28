# ReconhecimentoFacialRaspberry
Sistema de reconhecimento facial em Python para Raspberry Pi. Funcionalidades: 1) Captura de rostos 2) Treinamento do modelo LBPH 3) Identificação em tempo real. Usa OpenCV e Picamera2. Perfeito para controle de acesso, segurança e projetos IoT. Requer módulo de câmera.

# **🚀 Sistema Avançado de Reconhecimento Facial para Raspberry Pi**

![OpenCV](https://img.shields.io/badge/OpenCV-5.0%2B-5C3EE8?logo=opencv&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?logo=python&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Optimized-C51A4A?logo=raspberry-pi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-32CD32)
![CI](https://img.shields.io/badge/CI/CD-Ready-important)

## **📌 Visão Geral**
Sistema profissional de reconhecimento facial completo para Raspberry Pi, com pipeline de captura, treinamento e identificação em tempo real.

## **✨ Recursos**
- ✅ Pipeline completo de reconhecimento facial
- ✅ Otimizado para hardware limitado
- ✅ Sistema modular e escalável
- ✅ Documentação técnica completa

## **🛠 Tecnologias**
| Componente | Tecnologias |
|------------|-------------|
| **Núcleo** | Python 3.9+, OpenCV 4.5+ |
| **Hardware** | Raspberry Pi 4+, Picamera2 |
| **DevOps** | Docker, GitHub Actions |

## **🚀 Começando**

### Pré-requisitos
```bash
sudo apt update && sudo apt install python3-opencv python3-pip
pip install picamera2 numpy
```

### **Instalação**
Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
Execute o sistema:


cd seu-repositorio
python3 ReconhecimentoFacialRegistrarFace.py  # Para captura
python3 TreinamentoReconhecimentoFacial.py    # Para treino
python3 ReconhecimentoFinalFace.py            # Para reconhecimento

### **📂 Estrutura do Projeto**

├── faces/                   # Dataset facial

├── src/                     # Código fonte

│ ├── detection.py         # Detecção facial

│ ├── training.py          # Treinamento do modelo

│ └── recognition.py       # Reconhecimento

├── tests/                   # Testes automatizados

├── requirements.txt         # Dependências

└── LICENSE                  # Licença MIT

## **🤝 Como Contribuir**
Faça um Fork do projeto

Crie sua Branch (git checkout -b feature/NovaFeature)

Commit suas Mudanças (git commit -m 'Adiciona NovaFeature')

Push para a Branch (git push origin feature/NovaFeature)

Abra um Pull Request

### **📄 Licença**
Distribuído sob licença MIT. Veja LICENSE para mais informações.

### **📧 Contato**
kayky - kaykyrdepaula@gmail.com

Link do Projeto: https://github.com/kayky-ctrl/ReconhecimentoFacialRaspberry/

<div align="center"> <img src="https://img.shields.io/github/stars/kayky-ctrl/ReconhecimentoFacialRaspberry?style=social" alt="Stars"> <img src="https://img.shields.io/github/forks/kayky-ctrl/ReconhecimentoFacialRaspberry?style=social" alt="Forks"> </div>
