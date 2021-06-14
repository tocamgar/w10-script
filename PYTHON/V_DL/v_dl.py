# Programa para descarga de secuencias de archivos de video de internet
import tkinter as tk
from tkinter import ttk
import pyperclip as pp
import subprocess


def muestra_info(url):
    v_dur = '0'+subprocess.run('ffprobe -v error -show_entries format=duration -sexagesimal -of default=noprint_wrappers=1:nokey=1 \"'+url+'\"',
                               capture_output=True, text=True, shell=True).stdout.replace('\n', '').replace('\r', '')[:-3]  # Obtiene de ffprobe la duración del vídeo cargado en formato sexagesimal
    print("muestra_info: "+v_dur)
    fin_sec_var.set(v_dur)


def URL_pegar(url):
    global URL_var
    # Asigna un texto a URL_var y por tanto a la caja de entrada de texto asociada a URL_ent
    URL_var.set(url)
    muestra_info(URL_var.get())


def URL_borrar():
    global URL_var
    # Asigna un texto a URL_var y por tanto a la caja de entrada de texto asociada a URL_ent
    URL_var.set("")


def descargar(inicio,fin,url):
    print("comando descarga: ffmpeg -y -ss "+inicio+" -to "+fin+" -i \""+url+"\" -map "+"0:0"+" -map "+"0:1"+" -c copy d:/Vídeo/v_dl.mp4")


ventana = tk.Tk()
ventana.title("Descarga de secuencia de vídeo")

URL_var = tk.StringVar()
ini_sec_var = tk.StringVar()
fin_sec_var = tk.StringVar()

# Creando un objeto de clase PhotoImage
v_ico = tk.PhotoImage(file='V_DL.png')

# Seleccionar el icono de la aplicación
ventana.iconphoto(False, v_ico)

# Marco del URL del vídeo a descargar
mar_URL = ttk.Frame(ventana)
mar_URL.pack(padx=4, pady=4)

# Elementos del marco URL
URL_lbl = ttk.Label(mar_URL, text="URL del vídeo:").grid(row=0, column=0)
URL_ent = ttk.Entry(mar_URL, textvariable=URL_var,
                    width=150).grid(row=0, column=1)
URL_pega_btn = ttk.Button(mar_URL, text="PEGAR",
                          command=lambda: URL_pegar(pp.paste())).grid(row=0, column=2)
URL_borra_btn = ttk.Button(mar_URL, text="BORRAR",
                           command=URL_borrar).grid(row=0, column=3)

# Marco de la duración de la secuencia a descargar
mar_sec = ttk.Frame(ventana)
mar_sec.pack(padx=4, pady=4)

# Elementos del marco secuencia
ini_sec_lbl = ttk.Label(
    mar_sec, text="Inicio de secuencia:").grid(row=0, column=0)
ini_sec_ent = ttk.Entry(mar_sec, textvariable=ini_sec_var,
                        width=12).grid(row=0, column=1)
ini_sec_var.set("00:00:00.000")
fin_sec_lbl = ttk.Label(mar_sec, text="Fin de secuencia").grid(row=0, column=2)
fin_sec_ent = ttk.Entry(mar_sec, textvariable=fin_sec_var,
                        width=12).grid(row=0, column=3)
fin_sec_var.set("00:00:00.000")

# Marco descarga
mar_des = ttk.Frame(ventana)
mar_des.pack(padx=4, pady=4)

# Elementos del marco descarga
des_btn = ttk.Button(mar_des, text="DESCARGAR",
                     command=lambda: descargar(ini_sec_var.get(),fin_sec_var.get(),URL_var.get())).grid(row=0, column=0)
ventana.mainloop()
