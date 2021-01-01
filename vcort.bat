@ECHO OFF
SET VIDEO=%1
SET VINI=%2
SET VFIN=%3
ffmpeg -ss %VINI% -to %VFIN% -i %VIDEO% -c copy %VIDEO:~0,-5%_.mp4