@ECHO OFF
SET FOTO=%1
SET AUDIO=%2
FOR %%A IN (%AUDIO%) DO SET NAUDIO="%%~nxA"
::format=yuv420p hace que se pueda reproducir en Whatsapp de Android
::-pix_fmt yuv420p es el alias de -vf format=yuv420p
::-profile:v baseline ocupa menos que main y funciona junto con yuv420p
::ffmpeg -loop 1 -i %FOTO% -i %AUDIO% -vf scale=512:288,format=yuv420p -profile:v baseline -b:v 80k -c:a copy -shortest %NAUDIO:~0,-5%_288p_80k_68k.mp4"
::ffmpeg -loop 1 -i %FOTO% -i %AUDIO% -vf scale=512:288,format=yuv420p -profile:v main -b:v 80k -c:a copy -shortest %NAUDIO:~0,-5%_288p_80k_68k.mp4"
ffmpeg -loop 1 -i %FOTO% -i %AUDIO% -vf format=yuv420p -profile:v baseline -b:v 80k -c:a copy -shortest %NAUDIO:~0,-5%_80k.mp4"
