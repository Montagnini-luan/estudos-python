import tkinter as tk
from tkinter import StringVar, messagebox
from tkinter import ttk
from tkinter import font

class TemporizadorApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Temporizador')
        self.janela.geometry('400x250')
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
        estilo_entrada = ttk.Style()
        estilo_entrada.configure('TEntry', font=('Helvetica', 12), padding=6)

        self.label_tempo = tk.Label(
            self.janela, textvariable=self.tempo_texto,
            font=('Helvetica', 48), bg='#2E3B4E', fg='#FFFFFF'
        )
        self.label_tempo.pack(pady=20)

        self.entrada_tempo = tk.Entry(self.janela, font=('Helvetica', 12))
        self.entrada_tempo.pack(pady=20)
        self.entrada_tempo.insert(0, '00:00:00')

        frame_botoes = tk.Frame(self.janela, bg='#2E3B4E')
        frame_botoes.pack(pady=10)

        self.botao_iniciar = tk.Button(frame_botoes, text='Iniciar', command=self.iniciar)
        self.botao_iniciar.grid(row=0, column=0, padx=5)

        self.botao_pausar = tk.Button(frame_botoes, text='Pausar', command=self.pausar)
        self.botao_pausar.grid(row=0, column=1, padx=5)

        self.botao_reiniciar = tk.Button(frame_botoes, text='Reiniciar', command=self.reiniciar)
        self.botao_reiniciar.grid(row=0, column=2, padx=5)

    def iniciar(self):
        if not self.em_execucao:
            if self.tempo_segundos == 0:
                tempo_inicial = self.entrada_tempo.get()
                self.tempo_segundos = self.converter_para_segundos(tempo_inicial)
            else:
                tempo_inicial = self.tempo_texto.get()
                self.tempo_segundos = self.converter_para_segundos(tempo_inicial)
            if self.tempo_segundos > 0:
                self.em_execucao = True
                self.contar()
            else:
                messagebox.showerror('Erro', 'Insira um tempo válido')

    def contar(self):
        if self.em_execucao:
            if self.tempo_segundos > 0:
                self.tempo_segundos -= 1
                minutos, segundos = divmod(self.tempo_segundos, 60)
                horas, minutos = divmod(minutos, 60)
                tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}"
                self.tempo_texto.set(tempo_formatado)
                self.id_contador = self.janela.after(1000, self.contar)
            else:
                self.em_execucao = False
                self.tempo_texto.set('00:00:00')
                messagebox.showinfo('Tempo esgotado', 'O tempo acabou!')

    def converter_para_segundos(self, tempo_texto):
        try:
            horas, minutos, segundos = map(int, tempo_texto.split(':'))
            return horas * 3600 + minutos * 60 + segundos
        except ValueError:
            return 0

    def pausar(self):
        if self.em_execucao:
            self.em_execucao = False
            if self.id_contador:
                self.janela.after_cancel(self.id_contador)
                self.id_contador = None

    def reiniciar(self):
        self.pausar()
        self.tempo_segundos = 0
        self.tempo_texto.set('00:00:00')
        self.entrada_tempo.delete(0, tk.END)
        self.entrada_tempo.insert(0, '00:00:00')

if __name__ == '__main__':
    janela_principal = tk.Tk()
    app_cronometro = TemporizadorApp(janela_principal)
    janela_principal.mainloop()
