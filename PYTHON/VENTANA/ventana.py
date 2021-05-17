#PRIMERA VENTANA TKINTER

import tkinter as tk
from tkinter import Button, Label, filedialog, Entry
import subprocess
from tkinter.constants import INSERT
raíz=tk.Tk() 
ficheroVideo=""
etiqueta = Label(raíz, text="Fichero de video: ")
cajaTexto=Entry(raíz,width=100)

def elegirVideo():
  global ficheroVideo 
  global cajaTexto
  ficheroVideo = filedialog.askopenfilename(initialdir="d:\\Vídeos",title="Elige un vídeo",filetypes=( ("MP4","*.mp4"),("MATROSKA","*.mkv"),("TODOS LOS FICHEROS","*.*")))
  cajaTexto.insert(0,ficheroVideo)
  print (ficheroVideo)

def ff():
  global ficheroVideo
  subprocess.call("ffprobe -i " + ficheroVideo ,shell=True )

botónFichero=Button(text="Elige un vídeo",command=elegirVideo)
botónFFmpeg=Button(text="FFmpeg",command=ff)

etiqueta.grid(row=0,column=0,pady=10,padx=10)
cajaTexto.grid(row=0,column=1,padx=10)
botónFichero.grid(row=0,column=2,padx=10)
botónFFmpeg.grid(row=1,column=2)

raíz.mainloop()
