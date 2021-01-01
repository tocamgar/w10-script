::vtocamgar_06.bat
::UTILIZO %==% PARA INDENTAR DRAWTEXT
::A�ado un texto de t�tulo
::2020-12-31 10:43:40
::SET VIDEO="E:\V�deos\test.mp4"
::@ECHO OFF
SET VIDEO=%1
SET /P TITULO=Introduzca el t�tulo del video: 
ffmpeg ^
	-y ^
	-loglevel verbose ^
	-i %VIDEO% ^
	-vf ^
		  "scale=^
        width=-2:^
        height=360,^
      drawtext=^
        fontfile='C\:/Windows/Fonts/impact.ttf':^
        text=%TITULO%:^
        fontcolor=white:^
        borderw=1:^
        fontsize=18:^
        alpha=0.99:^
        x=(w-tw)/2:^
        y=th/4:^
        expansion=none, ^
      drawtext=^
        fontfile='C\:/Windows/Fonts/arial.ttf':^
        text='@tocamgar':^
        fontcolor=white:^
        borderw=1:^
        fontsize=18:^
        alpha=0.60:^
        x=w-tw-10:^
        y=h-th-10:^
        expansion=none" ^
	-map 0:v ^
	-map 0:a? ^
	-c:a aac ^
	-q:a 1 ^
	-ac 1 ^
	-c:v h264 ^
	-crf 30 ^
	%VIDEO:~0,-5%_tocamgar06.mp4"