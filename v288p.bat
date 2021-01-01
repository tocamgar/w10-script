@ECHO OFF
SET VIDEO=%1
ffmpeg -i %VIDEO% -vf scale=288*a:288 -b:v 150k -b:a 56k %VIDEO:~0,-5%_288p_150k_56k.mp4"
