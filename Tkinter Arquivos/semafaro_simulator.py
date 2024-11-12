import tkinter as tk

class Semafaro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Simulador de Semáforo')
        self.tela = tk.Canvas(janela, width=200, height=600, bg='black')
        self.tela.pack()
        
        self.cores = ['grey', 'grey', 'grey']
        self.luzes = []
        self.cores_ativas = ['red', 'yellow', 'green']
        self.intervalos = [2000, 1000, 2000]
        
        for i in range(3):
            x0, y0 = 50, 50 + 200 * i
            x1, y1 = 150, 150 + 200 * i
            luz = self.tela.create_oval(x0, y0, x1, y1, fill=self.cores[i], outline='white', width=2)
            self.luzes.append(luz)
            self.tela.tag_bind(luz, '<Button-1>', lambda event, idx=i: self.mudar_cor_manual(idx))
        
        self.estado_atual = 0
        self.ciclo_id = None
        self.mudar_cor_automaticamente()
        
    def mudar_cor_automaticamente(self):
        self.mudar_cor(self.estado_atual)
        self.estado_atual = (self.estado_atual + 1) % 3
        self.ciclo_id = self.janela.after(self.intervalos[self.estado_atual], self.mudar_cor_automaticamente)
            
    def mudar_cor_manual(self, idx):
        if self.ciclo_id:
            self.janela.after_cancel(self.ciclo_id)
            self.ciclo_id = None
            
        self.estado_atual = idx
        self.mudar_cor(self.estado_atual)
        self.ciclo_id = self.janela.after(self.intervalos[self.estado_atual], self.mudar_cor_automaticamente)

    def mudar_cor(self, idx):
        for i in range(3):
            if i == idx:
                self.tela.itemconfig(self.luzes[i], fill=self.cores_ativas[i])
            else:
                self.tela.itemconfig(self.luzes[i], fill=self.cores[i])

def main():
    janela = tk.Tk()
    semafaro = Semafaro(janela)
    janela.mainloop()

if __name__ == '__main__':
    main() 
