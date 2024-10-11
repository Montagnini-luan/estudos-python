import tkinter as tk
from tkinter import StringVar, messagebox
from tkinter import ttk

class CronometroApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cronômetro")
        self.janela.geometry('400x200')
        self.janela.configure(bg='#2E3B4E')
        self.tempo_segundos = 0
        self.tempo_texto = StringVar()
        self.tempo_texto.set('00:00:00')
        self.em_execucao = False
        self.id_contador = None
        self.configurar_layout()

    def configurar_layout(self):
        estilo_botao = ttk.Style()
        estilo_botao.configure('TButton', font=('Helvetica', 12), padding=6)
        
        self.label_tempo = tk.Label(self.janela, textvariable=self.tempo_texto, font=('Helvetica', 48), bg='#2E3B4E', fg='#FFFFFF')
        self.label_tempo.pack(pady=20)

        frame_botoes = tk.Frame(self.janela, bg='#2E3B4E')
        frame_botoes.pack(pady=10)

        self.botao_iniciar = ttk.Button(frame_botoes, text='Iniciar', command=self.iniciar)
        self.botao_iniciar.grid(row=0, column=0, padx=5)

        self.botao_parar = ttk.Button(frame_botoes, text='Parar', command=self.parar)
        self.botao_parar.grid(row=0, column=1, padx=5)

        self.botao_reiniciar = ttk.Button(frame_botoes, text='Reiniciar', command=self.reiniciar)
        self.botao_reiniciar.grid(row=0, column=2, padx=5)

    def iniciar(self):
        if not self.em_execucao:
            self.em_execucao = True
            self.contar()

    def contar(self):
        if self.em_execucao:
            self.tempo_segundos += 1
            minutos, segundos = divmod(self.tempo_segundos, 60)
            horas, minutos = divmod(minutos, 60)
            tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}"
            self.tempo_texto.set(tempo_formatado)
            self.id_contador = self.janela.after(1000, self.contar)

    def parar(self):
        if self.em_execucao:
            self.em_execucao = False
            if self.id_contador:
                self.janela.after_cancel(self.id_contador)
                self.id_contador = None

    def reiniciar(self):
        self.parar()
        self.tempo_segundos = 0
        self.tempo_texto.set('00:00:00')

if __name__ == '__main__':
    janela_principal = tk.Tk()
    app_cronometro = CronometroApp(janela_principal)
    janela_principal.mainloop()
