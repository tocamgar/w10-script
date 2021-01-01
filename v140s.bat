@ECHO OFF
SET VIDEO=%1
SET VDURA=%2
SET AVELO=%3
ffmpeg -i %VIDEO% -vf "setpts=%VDURA%*PTS" -af "atempo=%AVELO%" -b:v 200k -b:a 56k  %VIDEO:~0,-5%_140s.mp4"