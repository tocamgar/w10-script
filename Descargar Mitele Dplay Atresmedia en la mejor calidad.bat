@ECHO OFF
:top
cls
color 0b
ECHO -------DESCARGAR DE DPLAY-MITELE-ATRESMEDIA------
ECHO CANAL DE TELEGRAM

@echo off
echo.

SET /P URL=Introduzca la URL que desea descargar:

@echo off
echo.

SET /P TITULO=Introduzca el titulo del capitulo:

@echo off
echo.

ECHO Descargando capitulo..
streamlink "%URL%" best -o "%TITULO%.mp4"

pause
goto top
