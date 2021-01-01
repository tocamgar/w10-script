#! /bin/sh
#00 RECORTAR A 38 SEGUNDOS,REESCALAR A 512p ANCHO, RECODIFICAR Y COLOCAR LOGO
#################################################################################################
entrada_v="/mnt/e/Vídeos/CLOACAS INTERIOR/JUEZ SALVADOR ALBA VICTORIA ROSELL/SEIS AÑOS DE CÁRCEL PARA EL JUEZ ALBA POR CONFABULAR CONTRA LA DIPUTADA DE PODEMOS VICTORIA ROSELL.mp4"
entrada_a="/mnt/e/Vídeos/CLOACAS INTERIOR/JUEZ SALVADOR ALBA VICTORIA ROSELL/SEIS AÑOS DE CÁRCEL PARA EL JUEZ ALBA POR CONFABULAR CONTRA LA DIPUTADA DE PODEMOS VICTORIA ROSELL_.m4a"
logo="/mnt/e/Pictures/logo-cam_53x26.png"
salida="/mnt/e/Vídeos/CLOACAS INTERIOR/JUEZ SALVADOR ALBA VICTORIA ROSELL/SEIS AÑOS DE CÁRCEL PARA EL JUEZ ALBA POR CONFABULAR CONTRA LA DIPUTADA DE PODEMOS VICTORIA ROSELL_00.mp4"

ff -y \
  -t 38 -i "${entrada_v}" \
  -i "${entrada_a}" \
  -i "${logo}" \
  -filter_complex \
    " \
	[0:v] scale=512:-2:flags=bicubic [v1]; \
	[v1]drawtext=fontfile=/mnt/c/Windows/Fonts/impact.ttf :text='10/09/2019-JUEZ ALBA CONDENADO POR CONSPIRAR' :fontcolor=white :borderw=1 :fontsize=18 :alpha=0.67 :x=(w-tw)/2 :y=(th/2), \
	drawtext=fontfile=/mnt/c/Windows/Fonts/impact.ttf :text='CONTRA LA DIPUTADA DE PODEMOS VICTORIA ROSELL' :fontcolor=white :borderw=1 :fontsize=18 :alpha=0.67 :x=(w-tw)/2 :y=(th/2)+th+(th/4) [txt]; \
	[2:v]format=argb,colorchannelmixer=aa=0.5 [logo]; \
	[txt][logo]overlay=x=(main_w-overlay_w-5):y=(main_h-overlay_h-5)[v] \
	"\
  -map '[v]' \
  -map '1:a' \
  -c:a aac \
  -q:a 1 \
  -ac 1 \
  -c:v h264 \
  -crf 30 \
  "${salida}"