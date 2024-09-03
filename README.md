**Nebulous**

Aplicação Python simples que permite a manipulação de imagens e a extração de texto através de OCR (Reconhecimento Óptico de Caracteres) usando o Tesseract.


**ATENÇÃO!!!**

A acurácia base desse programa é risível de tão ruim. Só está sendo divulgado para uso público por ser divertido de se mexer. Sinta-se livre para melhorar, alterar e virá-lo de ponta cabeça! :)


**Requisitos**

*Certifique-se de ter os seguintes requisitos instalados no seu ambiente antes de executar o projeto:*

    >Python 3.x: A linguagem de programação necessária para executar o código.
    >Tesseract-OCR: Software de OCR necessário para realizar a extração de texto das imagens.
    
    >Tkinter: Biblioteca padrão do Python para criação de interfaces gráficas.
    >Pillow: Biblioteca Python Imaging Library (PIL) para abrir, manipular e salvar imagens.
    >Pytesseract: Biblioteca para acessar o Tesseract-OCR através do Python.
    >FPDF: Biblioteca para criar PDFs a partir do texto extraído.


**Configuração**

*Após instalar o Tesseract-OCR na sua máquina, configure o caminho do executável no script Python:*

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Nota: Altere o caminho tesseract_cmd para o local onde o Tesseract está instalado no seu sistema.


**Funcionalidades**

    >Abertura de Imagens: Permite selecionar e abrir imagens no formato JPG, PNG, etc.
    >Manipulação de Imagens:
        Rotacionar imagem.
        Inverter imagem horizontalmente ou verticalmente.
        Limpar a imagem carregada.
    >Transcrição:
        Exibição do texto extraído na interface.
        Copiar o texto para a área de transferência.
        Salvar o texto como um arquivo PDF.


**Como Usar**

   > Execute o script Python.
   > Use o botão "+" para carregar uma imagem.
   > Manipule a imagem utilizando os botões disponíveis (Rotacionar, Inverter).
   > Clique em "✎ TRANSCREVER" para realizar o OCR e extrair o texto da imagem.
   > Copie o texto utilizando o botão "📑 COPIAR" ou salve-o como PDF com "⬇📜 SALVAR COMO PDF".
