#PRUEVA DE FFMPEG A TRAVÉS DE PYTHON CON ENTORNO GRÁFICO
import tkinter as tk
import subprocess
ventana = tk.Tk()

canvas1 = tk.Canvas(ventana, width = 300, height = 300, bg = 'gray90', relief = 'raised')
canvas1.pack()

def ff ():
  subprocess.call("ffprobe -i d:/Vídeos/TEST.gif" ,shell=True )

boton01 = tk.Button(text='     ffprobe     ', command = ff, bg = 'red', fg = 'white', font = ('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=boton01)

ventana.mainloop()