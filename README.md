# ReconhecimentoFacialRaspberry
Sistema de reconhecimento facial em Python para Raspberry Pi. Funcionalidades: 1) Captura de rostos 2) Treinamento do modelo LBPH 3) Identificação em tempo real. Usa OpenCV e Picamera2. Perfeito para controle de acesso, segurança e projetos IoT. Requer módulo de câmera.
Sistema de Reconhecimento Facial - Raspberry Pi
https://img.shields.io/badge/OpenCV-5.0%252B-green https://img.shields.io/badge/Python-3.7%252B-blue https://img.shields.io/badge/Raspberry%2520Pi-Compatible-red

Um sistema completo de reconhecimento facial desenvolvido para Raspberry Pi, utilizando OpenCV e Picamera2. Ideal para projetos de controle de acesso, segurança e automação residencial.

📌 Funcionalidades
✔ Cadastro de rostos - Captura e armazena imagens faciais para treinamento
✔ Treinamento do modelo - Utiliza o algoritmo LBPH (Local Binary Patterns Histograms)
✔ Reconhecimento em tempo real - Identifica pessoas com exibição de confiança

🛠 Tecnologias Utilizadas
Python 3

OpenCV (Processamento de imagem e reconhecimento)

Picamera2 (Controle da câmera da Raspberry Pi)

NumPy (Manipulação de dados)

🚀 Como Usar
1. Pré-requisitos
Certifique-se de ter instalado:

bash
sudo apt update
sudo apt install python3-opencv python3-pip
pip install picamera2 numpy
2. Estrutura do Projeto
text
📁 projeto/
├── 📁 faces/               # Pasta para armazenar imagens capturadas
├── 📜 ReconhecimentoFacialRegistrarFace.py   # Captura rostos
├── 📜 TreinamentoReconhecimentoFacial.py     # Treina o modelo
└── 📜 ReconhecimentoFinalFace.py             # Reconhecimento em tempo real
3. Passo a Passo
🔹 Cadastrar Rostos
Execute o script de captura:

bash
python3 ReconhecimentoFacialRegistrarFace.py
Siga as instruções no terminal para registrar novas faces.

🔹 Treinar o Modelo
Após coletar imagens suficientes, execute:

bash
python3 TreinamentoReconhecimentoFacial.py
Isso gerará o arquivo trainer.yml.

🔹 Reconhecimento em Tempo Real
Execute o reconhecimento:

bash
python3 ReconhecimentoFinalFace.py
⚙ Personalização
Adicionar mais pessoas: Basta executar novamente o script de captura com um novo ID.

Ajustar sensibilidade: Modifique o limiar de confiança em ReconhecimentoFinalFace.py.

🔧 Solução de Problemas
"Classificador Haar não encontrado":
Verifique o caminho do arquivo XML ou instale:

bash
sudo apt install opencv-data
O arquivo estará em:

bash
/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml
📜 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

⭐ Dúvidas ou sugestões? Sinta-se à vontade para abrir uma issue!
