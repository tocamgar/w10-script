#! /bin/sh
#0_0 CÓDIGO ORIGINAL
#################################################################################################

v_ent="/mnt/e/Sonido/PODCAST/CARNE CRUDA/test.mp3"
logo="/mnt/e/Pictures/logo-cam_53x26_50a.png"
v_sal="/mnt/e/Users/tocam/PRUEBAS FFMPEG/ECUALIZADOR GRÁFICO - PRUEBA 01/RESULTADOS/vfreqs_0_8.mp4"
ffmpeg -y \
  -i "${audio}"\
  -i "${fondo}"\
  -i "${gradiente}"\
  -i "${mascara}"\
  -i "${logo}"\
  -filter_complex\
	"
	[2:v]scale=150x50[gradiente];\
	[3:v]scale=150x50[mascara_matriz_eq];\
	[gradiente][mascara_matriz_eq]alphamerge[matriz_eq];\
	[1:v]scale=-1:288,\
	drawtext=fontfile=/mnt/c/Windows/Fonts/impact.ttf :text='24-06-2020 \"INTRO\" CARNE CRUDA' :fontcolor=white :borderw=1 :fontsize=18 :alpha=1 :x=(w-tw)/2 :y=(th/4),\
	drawtext=fontfile=/mnt/c/Windows/Fonts/impact.ttf :text='\"BILL GATES, 5G, VACUNAS Y OTRAS CONSPIRACIONES\"' :fontcolor=white :borderw=1 :fontsize=18 :alpha=1 :x=(w-tw)/2 :y=((th/4)+(text_h)),\
	drawtext=fontfile=/mnt/c/Windows/Fonts/impact.ttf :text='https\://www.eldiario.es/carnecruda/programas/bill-gates-vacunas-conspiraciones_132_6057174.html' :fontcolor=lightskyblue :borderw=1 :fontsize=10 :alpha=1 :x=(w-tw)/2 :y=(th/4)+(4*text_h)[fondo_txt];\
	[fondo_txt]split[fondo_txt][fondo_txt_2];\
	[fondo_txt_2][matriz_eq]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)-5,setsar=1[fondo_txt_matriz_eq];\
	[0:a]showfreqs=s=150x50:mode=bar:colors=WHITE:fscale=log[mascara_showfreqs];\
	[mascara_showfreqs]pad=512:288:(ow-iw)/2:oh-ih-5:black[mascara_showfreqs];\
	[fondo_txt][fondo_txt_matriz_eq][mascara_showfreqs]maskedmerge[v1];\
	[v1][4:v]overlay=x=(main_w-overlay_w-5):y=(main_h-overlay_h-5)[v]\
	"\
  -map '[v]'\
  -map '0:a'\
  -c:a copy\
  -t 10\
  "${salida}"
