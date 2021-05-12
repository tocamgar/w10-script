#PRUEBA DE ARRASTRAR A BAT
@echo off
setlocal enableExtensions disableDelayedExpansion

echo Command line: %0 %*
echo Command line argument 1: %~1
echo Command line argument 2: "%~2"
pause

endlocal
goto :eof