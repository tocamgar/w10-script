@ECHO OFF
SETLOCAL  ENABLEDELAYEDEXPANSION
SET N=0
for /f "tokens=*" %%W in ('youtube-dl -g %1') do (
  SET /A N=!N!+1
  SET URL_!N!=%%W
  ECHO URL_!N!
  )
ffmpeg -i "!URL_1!" -i "!URL_2!" -c copy %2