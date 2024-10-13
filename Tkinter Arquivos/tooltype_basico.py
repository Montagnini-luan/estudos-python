import tkinter as tk
from tkinter import ttk

class CaixaDeDica:
    def __init__(self, widget, texto=''):
        self.widget = widget
        self.texto = texto
        self.janela_dica = None

    def mostrar_dica(self, x, y):
        self.janela_dica = jd = tk.Toplevel(self.widget)
        jd.wm_overrideredirect(True)
        jd.wm_geometry(f'+{x}+{y}')
        label = tk.Label(
            jd, text=self.texto, background='#1e09a5',
            relief='solid', borderwidth=1, font=('tahoma', 20, 'bold'), fg='white'
        )
        label.pack(ipadx=10, ipady=5)

    def esconder_dica(self):
        if self.janela_dica:
            self.janela_dica.destroy()
            self.janela_dica = None


class TabelaComCaixaDeDica:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title('Tabela com Caixa de Dica')
        quadro = ttk.Frame(raiz)
        quadro.pack(pady=10, padx=10, fill='both', expand=True)

        self.tabela = ttk.Treeview(
            quadro, columns=('Nome', 'Idade', 'Profissão'), show='headings', style='Estilo.Treeview'
        )
        self.tabela.heading('Nome', text='Nome')
        self.tabela.heading('Idade', text='Idade')
        self.tabela.heading('Profissão', text='Profissão')
        self.tabela.pack(fill='both', expand=True)

        estilo = ttk.Style()
        estilo.configure('Estilo.Treeview', font=('tahoma', 20), rowheight=30)
        estilo.configure('Estilo.Treeview.Heading', font=('tahoma', 20, 'bold'))

        dados = [
            ('Luan', 25, 'Programador'),
            ('Maria', 28, 'Designer'),
            ('João', 40, 'Analista'),
            ('Ana', 30, 'Engenheira')
        ]
        for item in dados:
            self.tabela.insert('', 'end', values=item)

        self.tabela.bind('<Motion>', self.ao_mover_mouse)
        self.caixa_dica = None

    def ao_mover_mouse(self, evento):
        id_linha = self.tabela.identify_row(evento.y)
        if id_linha:
            item = self.tabela.item(id_linha)
            valores = item['values']
            texto_dica = f'Nome: {valores[0]}\nIdade: {valores[1]}\nProfissão: {valores[2]}'
            x, y, largura, altura = self.tabela.bbox(id_linha)

            if not self.caixa_dica:
                self.caixa_dica = CaixaDeDica(self.tabela, texto=texto_dica)
                self.caixa_dica.mostrar_dica(evento.x_root + 20, evento.y_root + 20)
            else:
                self.caixa_dica.esconder_dica()
                self.caixa_dica = CaixaDeDica(self.tabela, texto=texto_dica)
                self.caixa_dica.mostrar_dica(evento.x_root + 20, evento.y_root + 20)
        else:
            if self.caixa_dica:
                self.caixa_dica.esconder_dica()
                self.caixa_dica = None

if __name__ == '__main__':
    raiz = tk.Tk()
    app = TabelaComCaixaDeDica(raiz)
    raiz.mainloop()
