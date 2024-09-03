import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

#SETAR O EXECUTÁVEL DO TESSERACT: USE O SEU CAMINHO AQUI
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#JANELA PRINCIPAL
root = tk.Tk()
root.title("Nebulous v1.0")
root.geometry("1920x1080")
root.state('zoomed')
root.configure(bg="#2e2e2e")

#ESTILO DOS BOTÕES
btn_style = {"bg": "#4CAF50", "fg": "white", "font": ("Arial", 20, "bold"), "relief": "raised", "bd": 3, "width": 0, "height": 0}
label_style = {"bg": "#1e1e1e", "fg": "white", "font": ("Arial", 10), "bd": 2, "relief": "groove", "padx": 5, "pady": 5}
text_style = {"bg": "#1e1e1e", "fg": "white", "font": ("Consolas", 10)}

img = None

#SELECIONAR E ABRIR IMAGEM
def open_image():
    global img, img_tk, file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((600, 600))
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk
        #EXIBE INFORMAÇÕES DA IMAGEM
        display_image_info()
        #TORNA AS INFORMAÇÕES E BOTÕES VISIVEIS
        name_label.pack(side="top", pady=5)
        dimensions_label.pack(side="top", pady=5)
        open_btn.pack(side="left", padx=5)
        clear_btn.pack(side="left", padx=5)
        rotate_btn.pack(side="left", padx=20)
        flip_h_btn.pack(side="left", padx=5)
        flip_v_btn.pack(side="left", padx=5)

#INFORMAÇÕES DA IMAGEM
def display_image_info():
    img_name = file_path.split("/")[-1]
    img_dimensions = f"{img.size[0]} x {img.size[1]}"
    name_label.config(text=f"{img_name}")
    dimensions_label.config(text=f"{img_dimensions}")

#REALIZAR O OCR
def perform_ocr():
    if img:
        text = pytesseract.image_to_string(img, lang='por')
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, text)

#ROTACIONAR A IMAGEM
def rotate_image():
    global img, img_tk
    if img:
        img = img.rotate(90, expand=True)
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk
        #ATUALIZA AS DIMENSÕES (BUGA CASO NÃO)
        display_image_info()

#APAGAR A IMAGEM
def clear_image():
    global img, img_tk
    img = None
    panel.config(image=placeholder)
    panel.image = placeholder
    name_label.pack_forget()
    dimensions_label.pack_forget()

#INVERTE HORIZONTALMENTE
def flip_image_horizontal():
    global img, img_tk
    if img:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk

#INVERTE VERTICALMENTE
def flip_image_vertical():
    global img, img_tk
    if img:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk

#COPIAR TEXTO
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(text_box.get("1.0", tk.END))

#SALVAR COMO PDF
def save_as_pdf():
    from fpdf import FPDF
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        text = text_box.get("1.0", tk.END)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.output(file_path)

#COMPONENTES DA INTERFACE
top_frame = tk.Frame(root, bg="#2e2e2e")
top_frame.pack(side="top", pady=10)

image_frame = tk.Frame(root, bg="#2e2e2e")
image_frame.pack(side="left", padx=10)

details_frame = tk.Frame(image_frame, bg="#2e2e2e")
details_frame.pack(side="top", pady=5)

panel = tk.Label(image_frame, bg="#2e2e2e", width=600, height=600)
panel.pack(side="top", pady=10)

name_label = tk.Label(details_frame, **label_style)
name_label.pack_forget()  # Esconde o rótulo de nome inicialmente

dimensions_label = tk.Label(details_frame, **label_style)
dimensions_label.pack_forget()  # Esconde o rótulo de dimensões inicialmente

placeholder = ImageTk.PhotoImage(Image.new('RGB', (600, 600), color='#3e3e3e'))
panel.config(image=placeholder)

buttons_frame = tk.Frame(image_frame, bg="#2e2e2e")
buttons_frame.pack(side="top", pady=10)

open_btn = tk.Button(buttons_frame, text="➕", command=open_image, **btn_style)
open_btn.pack(side="left", padx=5)

clear_btn = tk.Button(buttons_frame, text="✖", command=clear_image, bg="red", fg="white", font=("Arial", 20, "bold"), relief="raised", bd=3, width=0, height=0)
clear_btn.pack(side="left", padx=5)

rotate_btn = tk.Button(buttons_frame, text="⟳", command=rotate_image, **btn_style)
rotate_btn.pack(side="left", padx=20)

flip_h_btn = tk.Button(buttons_frame, text="⇋", command=flip_image_horizontal, **btn_style)
flip_h_btn.pack(side="left", padx=5)

flip_v_btn = tk.Button(buttons_frame, text="⇵", command=flip_image_vertical, **btn_style)
flip_v_btn.pack(side="left", padx=5)

#BOTÃO: REALIZAR TRANSCRIÇÃO
ocr_btn = tk.Button(image_frame, text="✎ TRANSCREVER", command=perform_ocr, **btn_style)
ocr_btn.pack(side="top", pady=10)

#ÁREA DE TRANSCRIÇÃO
text_frame = tk.Frame(root, bg="#2e2e2e")
text_frame.pack(side="right", pady=10, padx=10, fill="both", expand=True)

text_box = tk.Text(text_frame, height=10, width=10, wrap="word", **text_style)
text_box.pack(side="bottom", pady=10, padx=10, fill="both", expand=True)

#BOTÕES: COPIAR & SALVAR COMO PDF
text_buttons_frame = tk.Frame(text_frame, bg="#2e2e2e")
text_buttons_frame.pack(side="top", pady=5)

copy_btn = tk.Button(text_buttons_frame, text="📑 COPIAR", command=copy_text, **btn_style)
copy_btn.pack(side="left", padx=5)

pdf_btn = tk.Button(text_buttons_frame, text="⬇📜 SALVAR COMO PDF", command=save_as_pdf, **btn_style)
pdf_btn.pack(side="left", padx=5)

root.mainloop()