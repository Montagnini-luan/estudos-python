import tkinter as tk
from tkinter import messagebox
import pandas as pd
from tkinter import ttk

class Urna:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Urna Eletrônica')
        self.janela.geometry('800x600')
        
        # Tenta carregar os candidatos do arquivo Excel com o formato correto
        try:
            self.candidatos = pd.read_excel('Urna.xlsx')
            # Renomeia a coluna 'Candidato' para 'Nome' para manter compatibilidade
            self.candidatos = self.candidatos.rename(columns={'Candidato': 'Nome'})
            # Adiciona a coluna 'Número' caso não exista
            if 'Número' not in self.candidatos.columns:
                self.candidatos['Número'] = range(1, len(self.candidatos) + 1)
            self.votos = {row['Nome']: row['Votos'] for _, row in self.candidatos.iterrows()}
        except Exception as e:
            print(f"Erro ao carregar arquivo: {e}")
            self.candidatos = pd.DataFrame(columns=['Nome', 'Número', 'Votos'])
            self.votos = {}
        
        self.criar_widgets()
        
    def criar_widgets(self):
        # Frame principal
        self.frame_principal = tk.Frame(self.janela)
        self.frame_principal.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Frame dos candidatos
        self.frame_candidatos = tk.LabelFrame(self.frame_principal, text='Candidatos')
        self.frame_candidatos.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        # Treeview para candidatos
        colunas = ('nome', 'numero', 'votos')
        self.tree = ttk.Treeview(self.frame_candidatos, columns=colunas, show='headings')
        
        # Definindo as colunas
        self.tree.heading('nome', text='Nome')
        self.tree.heading('numero', text='Número')
        self.tree.heading('votos', text='Votos')
        
        # Configurando o tamanho das colunas
        self.tree.column('nome', width=200)
        self.tree.column('numero', width=100)
        self.tree.column('votos', width=100)
        
        # Adicionando scrollbar
        scrollbar = ttk.Scrollbar(self.frame_candidatos, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Empacotando a tree e scrollbar
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Frame dos botões
        self.frame_botoes = tk.Frame(self.frame_principal)
        self.frame_botoes.pack(side='right', fill='y', padx=5, pady=5)
        
        # Botões
        tk.Button(self.frame_botoes, text='Adicionar Candidato', 
                 command=self.adicionar_candidato).pack(fill='x', pady=2)
        tk.Button(self.frame_botoes, text='Remover Candidato', 
                 command=self.remover_candidato).pack(fill='x', pady=2)
        tk.Button(self.frame_botoes, text='Votar', 
                 command=self.votar).pack(fill='x', pady=2)
        tk.Button(self.frame_botoes, text='Verificar Vencedor', 
                 command=self.verificar_vencedor).pack(fill='x', pady=2)
        tk.Button(self.frame_botoes, text='Mostrar Resultados', 
                 command=self.mostrar_resultados).pack(fill='x', pady=2)
        
        self.atualizar_lista()
        
    def atualizar_lista(self):
        # Limpa todos os itens da tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adiciona os candidatos ordenados por número
        for _, row in self.candidatos.sort_values('Número').iterrows():
            self.tree.insert('', 'end', values=(row['Nome'], row['Número'], row['Votos']))
    
    def adicionar_candidato(self):
        janela_add = tk.Toplevel(self.janela)
        janela_add.title('Adicionar Candidato')
        janela_add.geometry('300x150')
        
        tk.Label(janela_add, text='Nome:').pack()
        nome_entry = tk.Entry(janela_add)
        nome_entry.pack()
        
        tk.Label(janela_add, text='Número:').pack()
        numero_entry = tk.Entry(janela_add)
        numero_entry.pack()
        
        def confirmar():
            nome = nome_entry.get()
            numero = numero_entry.get()
            
            if nome and numero:
                novo_candidato = pd.DataFrame({'Nome': [nome], 'Número': [numero], 'Votos': [0]})
                self.candidatos = pd.concat([self.candidatos, novo_candidato], ignore_index=True)
                self.votos[nome] = 0
                self.atualizar_lista()
                janela_add.destroy()
        
        tk.Button(janela_add, text='Confirmar', command=confirmar).pack(pady=10)
    
    def remover_candidato(self):
        selecao = self.tree.selection()
        if selecao:
            item = self.tree.item(selecao[0])
            nome = item['values'][0]  # O nome é o primeiro valor
            self.candidatos = self.candidatos[self.candidatos['Nome'] != nome]
            del self.votos[nome]
            self.atualizar_lista()
    
    def votar(self):
        janela_voto = tk.Toplevel(self.janela)
        janela_voto.title('Votar')
        janela_voto.geometry('300x150')
        
        tk.Label(janela_voto, text='Número do Candidato:').pack()
        numero_entry = tk.Entry(janela_voto)
        numero_entry.pack()
        
        def confirmar_voto():
            numero = numero_entry.get()
            candidato = self.candidatos[self.candidatos['Número'] == numero]
            
            if not candidato.empty:
                nome = candidato.iloc[0]['Nome']
                self.votos[nome] += 1
                self.candidatos.loc[self.candidatos['Nome'] == nome, 'Votos'] += 1
                self.atualizar_lista()  # Atualiza a treeview imediatamente
                messagebox.showinfo('Sucesso', 'Voto computado com sucesso!')
                janela_voto.destroy()
            else:
                messagebox.showerror('Erro', 'Candidato não encontrado!')
        
        tk.Button(janela_voto, text='Confirmar', command=confirmar_voto).pack(pady=10)
    
    def verificar_vencedor(self):
        if self.votos:
            vencedores = [candidato for candidato, votos in self.votos.items() if votos == max(self.votos.values())]
            if len(vencedores) > 1:
                messagebox.showinfo('Empate', 
                                  f'Empate entre {", ".join(vencedores)} com {max(self.votos.values())} votos cada!')
            else:
                messagebox.showinfo('Vencedor', 
                                  f'O vencedor é {vencedores[0]} com {max(self.votos.values())} votos!')
        else:
            messagebox.showinfo('Aviso', 'Não há votos registrados!')
    
    def mostrar_resultados(self):
        janela_resultados = tk.Toplevel(self.janela)
        janela_resultados.title('Resultados')
        janela_resultados.geometry('400x300')
        
        texto_resultados = tk.Text(janela_resultados)
        texto_resultados.pack(fill='both', expand=True, padx=10, pady=10)
        
        resultados = "RESULTADOS DA VOTAÇÃO\n\n"
        for nome, votos in self.votos.items():
            resultados += f"Candidato: {nome}\nVotos: {votos}\n\n"
        
        texto_resultados.insert('1.0', resultados)
        texto_resultados.config(state='disabled')
    
    def __del__(self):
        # Prepara o DataFrame para salvar
        df_para_salvar = self.candidatos[['Nome', 'Votos']]
        df_para_salvar = df_para_salvar.rename(columns={'Nome': 'Candidato'})
        # Salva os dados ao fechar o programa
        df_para_salvar.to_excel('Urna.xlsx', index=False)

def main():
    janela = tk.Tk()
    urna = Urna(janela)
    janela.protocol("WM_DELETE_WINDOW", lambda: (urna.__del__(), janela.destroy()))
    janela.mainloop()

if __name__ == '__main__':
    main()
