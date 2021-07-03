import tkinter as tk
from tkinter import StringVar, filedialog, ttk
import subprocess
import pathlib as Path
import json
import datetime
import pyperclip as pp


def elige_video():
    global v_json_obj
    global initial_dir
    # Seleccionamos el vídeo de entrada.
    video = filedialog.askopenfilename(initialdir=initial_dir, title="Elige un vídeo",
                                       filetypes=(("TODOS LOS FICHEROS", "*.*"),
                                                  ("MATROSKA", "*.mkv"),
                                                  ("TELESTREAM", "*.ts"),
                                                  ("WebM", "*.webm"),
                                                  ("MP4", "*.mp4")))
    if not video == '':
        v_json_str = subprocess.run('ffprobe -loglevel 0 -print_format json -show_format \"' + video + '\"', capture_output=True, text=True).stdout
        v_json_obj = json.loads(v_json_str)
        v_ent_var.set(video)
        initial_dir = str(Path.PurePath(video).parent)
        v_dur_segundos = float(v_json_obj['format']['duration'])
        v_dur_sexagesimal = str(datetime.timedelta(seconds=v_dur_segundos))[:-3]
        fin_sec_var.set(v_dur_sexagesimal)
        btn_FFplay.config(state='normal')
        btn_FFmpeg.config(state='normal')

def a_sexagesimal(segundos):
    # return str(datetime.timedelta(seconds=segundos))
    '''    segundos , mseg = segundos.split('.')
    segundos = int(segundos)
    minutos = segundos // 60
    segundos = segundos % 60
    horas = minutos // 60
    minutos = minutos % 60
    if horas < 10:
        horas = '0' + str(horas)
    if minutos < 10:
        minutos = '0' + str(minutos)
    segundos = str(segundos) + '.' + mseg
    print (horas + ':' + minutos + ':' + segundos)
    return horas + ':' + minutos + ':' + segundos '''

def ent_v_ent_focus(e):
    widget=app.focus_get()
    print(widget, ' tiene el foco')
    
def muestra_delogo_2():
    if marco_2_btn['text']=='2 >>':
    	marco_delogo_2.grid(row=0, column=1, padx=4)
    	marco_2_btn.config(text='2 <<', bg='red',fg='white')
    else:
        marco_delogo_2.grid_forget()
        marco_2_btn.config(text='2 >>', bg='green', fg='white')
    
def muestra_delogo_3():
    if btn_marco_3['text']=='3 >>':
    	marco_delogo_3.grid(row=0, column=2, padx=4)
    	btn_marco_3.config(text='3 <<', bg='red', fg='white')
    else:
        marco_delogo_3.grid_forget()
        btn_marco_3.config(text='3 >>', bg='green', fg='white')


def previsualiza():
    video = v_ent_var.get()
    v_json_str = subprocess.run('ffprobe -loglevel 0 -print_format json -show_format \"' +
                           video + '\"', capture_output=True, text=True).stdout
    v_json_obj = json.loads(v_json_str)
    v_dur = v_json_obj['format']['duration']
    print('\"' + v_dur + '\"')


def codifica():
    pass


# DECLARACIÓN DE LA VENTANA
app = tk.Tk()
app.title('Elimina la marca de agua (logo) de los vídeos')
# Creando un objeto de clase PhotoImage
app_ico = tk.PhotoImage(file='VDELOGO_ICO.png')
# Seleccionar el icono de la aplicación
app.iconphoto(False, app_ico)

# ESTILOS
'''estilo_rojo=ttk.Style()
#estilo_rojo.map('rojo.TButton', foregr)
#estilo_verde = {'fg': 'white', 'bg': 'green', 'activebackground':'gray71', 'activeforeground': 'gray71'}
estilo_rojo.configure('Button',
                      background = 'red',
                      foreground='white')
'''
# MARCO VIDEO DE ENTRADA
marco_v_ent = ttk.Frame(app)
marco_v_ent.pack(padx=4, pady=4)

# ELEMENTOS DE VIDEO DE ENTRADA
eti_v_ent = ttk.Label(marco_v_ent, text="Fichero de video:")
eti_v_ent.grid(row=0, column=0, pady=5)

v_json_obj = ''
initial_dir = str(Path.PurePath("d:\\Vídeos"))

v_ent_var = StringVar()
v_ent_var.set('')

ent_v_ent = tk.Entry(marco_v_ent, width=150, textvariable=v_ent_var)
ent_v_ent.grid(row=0, column=1, padx=4)
ent_v_ent.bind('<FocusOut>', ent_v_ent_focus)

btn_v_ent = ttk.Button(marco_v_ent, text="Elige un vídeo", command=elige_video)
btn_v_ent.grid(row=0, column=3)

# MARCO ESCALA - SECUENCIA
marco_escala_secuencia = ttk.Frame(app)
marco_escala_secuencia.pack(padx=4, pady=4)
# MARCO ESCALA
marco_escala = ttk.Labelframe(marco_escala_secuencia, text='TAMAÑO DE VIDEO', labelanchor='n')
marco_escala.grid(row=0, column=0, sticky='w', padx=4, pady=4)

# ESCALA
eti_tamaño = ttk.Label(marco_escala, text="Ancho:")
eti_tamaño.grid(row=0, column=0, padx=4, pady=4)

tamaño_h_var = StringVar(value='640')
spin_tamaño_h = ttk.Spinbox(marco_escala, width=5, from_=0, to=1920, justify='center', textvariable=tamaño_h_var)
spin_tamaño_h.grid(row=1, column=0, padx=4, pady=4)

eti_tamaño_x = ttk.Label(marco_escala, text="Alto:")
eti_tamaño_x.grid(row=0, column=1, padx=4, pady=4)

tamaño_v_var = StringVar(value='360')
spin_tamaño_v = ttk.Spinbox(marco_escala, width=5, from_=0, to=1080, justify='center', textvariable=tamaño_v_var)
spin_tamaño_v.grid(row=1, column=1, padx=4, pady=4)

# MARCO SECUENCIA
marco_secuencia = ttk.Labelframe(marco_escala_secuencia, text='SECUENCIA DEL VIDEO', labelanchor='n')
marco_secuencia.grid(row=0, column=1, sticky='w', padx=4, pady=4)

# SECUENCIA
eti_ini_sec = ttk.Label(marco_secuencia, text="Inicio secuencia:")
eti_ini_sec.grid(row=0, column=0, padx=4,pady=4)

ini_sec_var = StringVar(value="00:00:00.000")
ent_ini_sec = ttk.Entry(marco_secuencia, width=12, textvariable=ini_sec_var)
ent_ini_sec.grid(row=1, column=0, padx=4, pady=4)

eti_fin_sec = ttk.Label(marco_secuencia, text="Fin secuencia:")
eti_fin_sec.grid(row=0, column=1, padx=4, pady=4)

fin_sec_var = StringVar(value="00:00:00.000")
ent_fin_sec = ttk.Entry(marco_secuencia, width=12, textvariable=fin_sec_var)
ent_fin_sec.grid(row=1, column=1, padx=4, pady=4)

# MARCO DELOGO
marco_delogo = ttk.Labelframe(app, text='COORDENADAS DEL FILTRO DELOGO')
marco_delogo.pack(fill='x', padx=4, pady=4)

marco_delogo_1 = ttk.Labelframe(marco_delogo, text='1')
marco_delogo_1.grid(row=0,column=0,padx=4, pady=4)

marco_delogo_2 = ttk.Labelframe(marco_delogo, text='2')

marco_delogo_3 = ttk.Labelframe(marco_delogo, text='3')
#marco_delogo_3.grid(row=0, column=2, padx=4)

# ELEMENTOS DELOGO 1
dlg1_x_eti = ttk.Label(marco_delogo_1, text="X:", padding=5)
dlg1_x_eti.grid(row=0, column=0, padx=4)

dlg1_x_var = StringVar(value='0')
dlg1_x_spin = ttk.Spinbox(marco_delogo_1, width=5, from_=0, to=1920, textvariable=dlg1_x_var)
dlg1_x_spin.grid(row=1, column=0, padx=4)

dlg1_y_eti = ttk.Label(marco_delogo_1, text="Y:", padding=5)
dlg1_y_eti.grid(row=0, column=1, padx=4)

dlg1_y_var = StringVar(value='0')
dlg1_y_spin = ttk.Spinbox(marco_delogo_1, width=5, from_=0, to=1080, textvariable=dlg1_y_var)
dlg1_y_spin.grid(row=1, column=1, padx=4)

dlg1_an_eti = ttk.Label(marco_delogo_1, text="ANCHO:", padding=5)
dlg1_an_eti.grid(row=0, column=2, padx=4)

dlg1_an_var = StringVar(value='0')
dlg1_an_spin = ttk.Spinbox(marco_delogo_1, width=5, from_=0, to=1920, textvariable=dlg1_an_var)
dlg1_an_spin.grid(row=1, column=2, padx=4)

dlg1_al_eti = ttk.Label(marco_delogo_1, text="ALTO:", padding=5)
dlg1_al_eti.grid(row=0, column=3, padx=4)

dlg1_al_var = StringVar(value='0')
dlg1_al_spin = ttk.Spinbox(marco_delogo_1, width=5, from_=0, to=1080, textvariable=dlg1_al_var)
dlg1_al_spin.grid(row=1, column=3, padx=4)

marco_2_btn = tk.Button(marco_delogo_1, padx=4, text='2 >>', bg='green', fg='white', command=muestra_delogo_2)
marco_2_btn.grid(row=0, column=4,rowspan=2, padx=4)

# ELEMENTOS DELOGO 2
eti_x_2 = ttk.Label(marco_delogo_2, text="X:", padding=5)
eti_x_2.grid(row=0, column=0)

x_var_2 = StringVar(value='0')

entry_x_2 = ttk.Entry(marco_delogo_2, width=5, textvariable=x_var_2)
entry_x_2.grid(row=0, column=1)

eti_y_2 = ttk.Label(marco_delogo_2, text="Y:", padding=5)
eti_y_2.grid(row=0, column=2)

y_var_2 = StringVar(value='0')
entry_y_2 = ttk.Entry(marco_delogo_2, width=5, textvariable=y_var_2)
entry_y_2.grid(row=0, column=3)

eti_ancho_2 = ttk.Label(marco_delogo_2, text="ANCHO:", padding=5)
eti_ancho_2.grid(row=0, column=4)

ancho_var_2 = StringVar(value='0')

entry_ancho_2 = ttk.Entry(marco_delogo_2, width=5, textvariable=ancho_var_2)
entry_ancho_2.grid(row=0, column=5)

eti_alto_2 = ttk.Label(marco_delogo_2, text="ALTO:", padding=5)
eti_alto_2.grid(row=0, column=6)

alto_var_2 = StringVar(value='0')

entry_alto_2 = ttk.Entry(marco_delogo_2, width=5, textvariable=alto_var_2)
entry_alto_2.grid(row=0, column=7)

btn_marco_3 = tk.Button(marco_delogo_2, padx=4, text='3 >>',
                        bg='green', fg='white', command=muestra_delogo_3)
btn_marco_3.grid(row=0, column=8)

# ELEMENTOS DELOGO 3
eti_x_3 = ttk.Label(marco_delogo_3, text="X:", padding=5)
eti_x_3.grid(row=0, column=0)

x_var_3 = StringVar(value='0')

entry_x_3 = ttk.Entry(marco_delogo_3, width=5, textvariable=x_var_3)
entry_x_3.grid(row=0, column=1)

eti_y_3 = ttk.Label(marco_delogo_3, text="Y:", padding=5)
eti_y_3.grid(row=0, column=2)

y_var_3 = StringVar(value='0')
entry_y_3 = ttk.Entry(marco_delogo_3, width=5, textvariable=y_var_3)
entry_y_3.grid(row=0, column=3)

eti_ancho_3 = ttk.Label(marco_delogo_3, text="ANCHO:", padding=5)
eti_ancho_3.grid(row=0, column=4)

ancho_var_3 = StringVar(value='0')

entry_ancho_3 = ttk.Entry(marco_delogo_3, width=5, textvariable=ancho_var_3)
entry_ancho_3.grid(row=0, column=5)

eti_alto_3 = ttk.Label(marco_delogo_3, text="ALTO:", padding=5)
eti_alto_3.grid(row=0, column=6)

alto_var_3 = StringVar(value='0')

entry_alto_3 = ttk.Entry(marco_delogo_3, width=5, textvariable=alto_var_3)
entry_alto_3.grid(row=0, column=7)

# MARCO TÍTULO - LOGO
marco_titulo = ttk.Labelframe(app, text='TÍTULO Y LOGOTIPO')
marco_titulo.pack(fill='x', padx=4, pady=4)

# TÍTULO
eti_titulo = ttk.Label(marco_titulo, text="Título:", padding=4)
eti_titulo.grid(row=0, column=0)

titulo_var = StringVar()
titulo_var.set('')
entry_titulo = ttk.Entry(marco_titulo, textvariable=titulo_var, width=80)
entry_titulo.grid(row=0, column=1)

# LOGO
eti_logo = ttk.Label(marco_titulo, text="Logotipo:", padding=4)
eti_logo.grid(row=0, column=2)

logo_var=StringVar(value='@tocamgar')
entry_logo = ttk.Entry(marco_titulo, textvariable=logo_var)
entry_logo.grid(row=0, column=3)

# MARCO OPCIONES SALIDA
marco_op_salida = ttk.Frame(app)
marco_op_salida.pack(fill='x',padx=4, pady=4)

marco_op_video = ttk.Labelframe(marco_op_salida, text='OPCIONES DE VIDEO', padding=4)
marco_op_video.grid(row=0, column=0, padx=4)

marco_op_audio = ttk.Labelframe(marco_op_salida, text='OPCIONES DE VIDEO', padding=4)
marco_op_audio.grid(row=0, column=1, padx=4)

# OPCIONES VIDEO DE SALIDA
eti_f_sal = ttk.Label(marco_op_video, text="Formato:", padding=4)
eti_f_sal.grid(row=0, column=0)

combo_f_sal = ttk.Combobox(marco_op_video, width=6, values=[".mp4",
														".mkv",
														".webm"])
combo_f_sal.current(0)
combo_f_sal.grid(row=0, column=1)

eti_crf = ttk.Label(marco_op_video, text="CRF:", padding=4)
eti_crf.grid(row=0, column=2)

spin_crf_mp4 = ttk.Spinbox(marco_op_video, width=4, from_=0, to=51, increment=1, state='readonly')
spin_crf_mp4.set(25)
spin_crf_mp4.grid(row=0, column=3)

eti_aud_sal = ttk.Label(marco_op_audio, text="Formato:", padding=4)
eti_aud_sal.grid(row=0, column=0)

combo_aud_sal = ttk.Combobox(marco_op_audio, width=11, values=["aac",
														   "libmp3lame"])
combo_aud_sal.current(0)
combo_aud_sal.grid(row=0, column=1)

eti_q_a = ttk.Label(marco_op_audio, text="q:a ", padding=4)
eti_q_a.grid(row=0, column=2)

spin_q_aac = ttk.Spinbox(marco_op_audio, width=4, from_=0.1, to=2, increment=0.1, state='readonly')
spin_q_aac.set(0.5)
spin_q_aac.grid(row=0, column=3)

eti_stereo = ttk.Label(marco_op_audio, text="Canales:", padding=4)
eti_stereo.grid(row=0, column=4)

combo_stereo = ttk.Combobox(marco_op_audio, width=7, values=['MONO',
                                						 'STEREO'])
combo_stereo.current(0)
combo_stereo.grid(row=0, column=5)

# MARCO FFMPEG
marco_ffmpeg = ttk.Frame(app)
marco_ffmpeg.pack(ipadx=5, ipady=5)

# FFMPEG
btn_FFplay = ttk.Button(marco_ffmpeg, text="FFplay", command=previsualiza, state='disabled')
btn_FFplay.pack(side="left", pady=5)

btn_FFmpeg = ttk.Button(marco_ffmpeg, text="FFmpeg", command=codifica, state='disabled')
btn_FFmpeg.pack(side="left", pady=5)

# BUCLE PRINCIPAL
app.mainloop()
