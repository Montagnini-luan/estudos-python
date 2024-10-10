import tkinter as tk
from tkinter import StringVar
from datetime import datetime
import pytz

class RelogioMundialApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Relógio Mundial")
        self.janela.geometry('900x500')
        self.janela.configure(bg='#1E2A38')

        self.fusos_horarios = {
            'UTC': 'Etc/UTC',
            'Nova Iorque': 'America/New_York',
            'São Paulo': 'America/Sao_Paulo',
            'Londres': 'Europe/London',
            'Paris': 'Europe/Paris',
            'Tóquio': 'Asia/Tokyo',
            'Sidney': 'Australia/Sydney'
        }

        self.relogio_vars = {nome: StringVar() for nome in self.fusos_horarios.keys()}
        self.data_vars = {nome: StringVar() for nome in self.fusos_horarios.keys()}

        self.configurar_layout()
        self.atualizar_relogio()

    def configurar_layout(self):
        estilo_rotulo = {'font': ("Arial", 14, 'bold'), 'bg': "#1E2A38", 'fg': "#FFFFFF"}
        estilo_info = {'font': ("Arial", 14), 'bg': "#1E2A38", 'fg': "#B0BEC5"}
        estilo_hora = {'font': ("Arial", 14, 'bold'), 'bg': "#1E2A38", 'fg': "#00C1D2"}

        self.titulo = tk.Label(self.janela, text="Relógio Mundial", font=("Arial", 18, 'bold'), bg="#1E2A38", fg="#FFFFFF")
        self.titulo.pack(pady=10)
    
        frame_relogio = tk.Frame(self.janela, bg="#1E2A38")
        frame_relogio.pack(pady=20)

        for i, (cidade, _) in enumerate(self.fusos_horarios.items()):
            frame = tk.Frame(frame_relogio, bg="#1E2A38")
            frame.grid(row=i, column=0, padx=20, pady=5, sticky=tk.W)

            label_nome = tk.Label(frame, text=cidade, **estilo_rotulo)
            label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
            label_hora = tk.Label(frame, textvariable=self.relogio_vars[cidade], **estilo_hora)
            label_hora.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
            label_data = tk.Label(frame, textvariable=self.data_vars[cidade], **estilo_info)
            label_data.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

    def atualizar_relogio(self):
        for cidade, fuso in self.fusos_horarios.items():
            timezone = pytz.timezone(fuso)
            agora = datetime.now(timezone)
            hora_atual = agora.strftime('%H:%M:%S')
            data_atual = agora.strftime('%A, %d de %B de %Y')
            data_atual = self.traduzir_data(data_atual)

            self.relogio_vars[cidade].set(hora_atual)
            self.data_vars[cidade].set(data_atual)

        self.janela.after(1000, self.atualizar_relogio)

    def traduzir_data(self, data):
        traducoes = {
            'Monday': 'Segunda-feira',
            'Tuesday': 'Terça-feira',
            'Wednesday': 'Quarta-feira',
            'Thursday': 'Quinta-feira',
            'Friday': 'Sexta-feira',
            'Saturday': 'Sábado',
            'Sunday': 'Domingo',
            'January': 'Janeiro',
            'February': 'Fevereiro',
            'March': 'Março',
            'April': 'Abril',
            'May': 'Maio',
            'June': 'Junho',
            'July': 'Julho',
            'August': 'Agosto',
            'September': 'Setembro',
            'October': 'Outubro',
            'November': 'Novembro',
            'December': 'Dezembro'
        }

        for ingles, portugues in traducoes.items():
            data = data.replace(ingles, portugues)
        return data

if __name__ == '__main__':
    janela_principal = tk.Tk()
    app_relogio_mundial = RelogioMundialApp(janela_principal)
    janela_principal.mainloop()
