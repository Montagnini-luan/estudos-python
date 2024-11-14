import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import re

def gerar_qr_code():
    texto = entrada_texto.get("1.0", "end-1c").strip()
    
    if not texto:
        messagebox.showerror("Erro", "Digite um link ou texto para gerar o QR Code")
        return
    
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(texto)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save("qrcode.png")
    
    exibir_qr_code(img)

def exibir_qr_code(img):
    qr_imagem = Image.open("qrcode.png")
    qr_imagem = qr_imagem.resize((200, 200), Image.LANCZOS)
    qr_imagem_tk = ImageTk.PhotoImage(qr_imagem)
    label_qr_code.config(image=qr_imagem_tk)
    label_qr_code.image = qr_imagem_tk

def sanitizar_nome_arquivo(texto):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', texto)

def salvar_qr_code():
    texto = entrada_texto.get("1.0", "end-1c").strip()
    if not texto:
        messagebox.showerror("Erro", "Digite um link ou texto para gerar o QR Code")
        return
    
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(texto)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    nome_arquivo = sanitizar_nome_arquivo(texto)[:50]
    
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialfile=nome_arquivo)
    
    if caminho_arquivo:
        img.save(caminho_arquivo)
        messagebox.showinfo("Sucesso", "QR Code salvo com sucesso!")

janela = tk.Tk()
janela.title("Gerador de QR Code")
janela.configure(bg="#f0f0f0")
largura = 600
altura = 400

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicao_x = (largura_tela - largura) // 2
posicao_y = (altura_tela - altura) // 2

janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

frame_entrada = tk.Frame(janela, bg="#f0f0f0")
frame_entrada.pack(pady=10)

label_entrada = tk.Label(frame_entrada, text="Digite o link ou texto para gerar o QR Code:", bg="#f0f0f0", font=('helvetica', 12))
label_entrada.pack()

entrada_texto = tk.Text(frame_entrada, width=50, height=4, font=('helvetica', 12))
entrada_texto.pack(pady=5)

frame_botoes = tk.Frame(janela, bg="#f0f0f0")
frame_botoes.pack(pady=10)

botao_gerar = tk.Button(frame_botoes, text="Gerar QR Code", command=gerar_qr_code, bg="#007bff", fg="white", font=('helvetica', 12), relief=tk.RAISED, bd=2)
botao_gerar.pack(side=tk.LEFT, padx=5)

botao_salvar = tk.Button(frame_botoes, text="Salvar QR Code", command=salvar_qr_code, bg="#007bff", fg="white", font=('helvetica', 12), relief=tk.RAISED, bd=2)
botao_salvar.pack(side=tk.LEFT, padx=5)

label_qr_code = tk.Label(janela, bg="#f0f0f0")
label_qr_code.pack(pady=10)





janela.mainloop()
