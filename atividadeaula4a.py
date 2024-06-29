import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def grafico():
    estados= ['SP','RS','BA','PE','ES','MT','MS']
    pib = [150,300,500,800,150,300,900]
    pib.sort()

   # criando o grafico
    fig, ax = plt.subplots()
    ax.bar(estados,pib)

   # rótulos
    ax.set_xlabel('pib')
    ax.set_ylabel('estados')
    ax.set_title('GRAFICO DE PIB/ESTADO')
    ax.grid(True)
    
    canvas =  FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

   # Integração do grafico com o TKINTER

janela = tk.Tk()
janela.title('Estados')   

frame_grafico = tk.Frame(janela)
frame_grafico.pack()


btn = tk.Button(janela, text='mostrar grafico', command= grafico)
btn.pack(padx=10)


janela.mainloop()