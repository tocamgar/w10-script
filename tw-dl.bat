::@ECHO OFF
SETLOCAL  ENABLEDELAYEDEXPANSION
SET /P URL=Introduzca la direcci¢n del video: 
SET /P TITULO=Introduzca el t¡tulo del video: 
FOR /f "tokens=*" %%W in ('youtube-dl -g %URL%') do ffmpeg -i %%W -c copy "e:\V¡deos\%TITULO%.mp4"
MORE