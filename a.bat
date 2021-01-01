@echo off
::muestra lista de ficheros
::for %%a in ("E:\V¡deos\CURIOSAMENTE\CAPITALISMO O SOCIALISMO_64_56_288p_?.mp4") do echo.%%a
SETLOCAL ENABLEDELAYEDEXPANSION
set /A _num=0
::set /A _num +=1
for %%a in ("E:\V¡deos\CURIOSAMENTE\CAPITALISMO O SOCIALISMO_64_56_288p_?.mp4") do (
	set archivo=%%a
::	echo.!_num!
	echo.%archivo:~0,56%_140s!archivo:~-6!
::	ffmpeg -i "%%a" -b:v 64k -b:a 56k -vf "setpts=0.877078*PTS" -af "atempo=1.140150" "%archivo:~0,58%_140s_!_num!.mp4"
	set /A _num += 1
)