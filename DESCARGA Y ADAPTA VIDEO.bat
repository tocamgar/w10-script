@echo off
::echo %1
cd E:\V°deos\CURIOSAMENTE\
::for %%a in ("CAPITALISMO O SOCIALISMO_64_56_288p_140s_0.mp4") do ffprobe -v error -show_entries format=duration -sexagesimal -of default=noprint_wrappers=1:nokey=1 %%a>var.txt
for %%a in (%1) do ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 %%a>var.txt
::"ffprobe -v error -show_entries format=duration -sexagesimal -of default=noprint_wrappers=1:nokey=1 KITE SURF .mp4"> aux.txt
set /P _DURACI‡N_VIDEO=<var.txt 
echo.DURACI‡N: %_DURACI‡N_VIDEO%
SET /A _PARTES = %_DURACI‡N_VIDEO% / 140
::set /A _ENTERO = %_DURACI‡N_VIDEO%
::ECHO.DURACI‡N: %_ENTERO%
::SET /A _PARTES = %_ENTERO% / 140
echo.PARTES: "%_PARTES%"

::ffmpeg -i "https://youtu.be/MaKvo-3iWCo" -c copy "E:\V°deos\TODOS NAZIS.mp4"

::for %a in ("E:\V°deos\CURIOSAMENTE\CAPITALISMO O SOCIALISMO_64_56_288p_140s_0.mp4") do set /P var=ffprobe -v error -show_entries format=duration -sexagesimal -of default=noprint_wrappers=1:nokey=1 %a