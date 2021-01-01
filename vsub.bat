::@ECHO OFF
SET VIDEO=%1
SET SUBT=%VIDEO:~0,-5%.ass"
ffmpeg -y -i %VIDEO% -vf subtitles=%SUBT% -q 1 %VIDEO:~0,-5%_sub.mp4"