::vtocamgar_03.bat
::UTILIZO %==% PARA INDENTAR DRAWTEXT
::SET VIDEO="E:\V¡deos\test.mp4"
::@ECHO OFF
SET VIDEO=%1
ffmpeg ^
	-y ^
	-loglevel verbose ^
	-i %VIDEO% ^
	-vf ^
		  scale=^
%=			=%width=-2:^
%=			=%height=360,^
%=	=%drawtext=^
%=			=%fontfile='C\:/Windows/Fonts/arial.ttf':^
%=			=%text='@tocamgar':^
%=			=%fontcolor=white:^
%=			=%borderw=1:^
%=			=%fontsize=18:^
%=			=%alpha=0.60:^
%=			=%x=w-tw-10:^
%=			=%y=h-th-10:^
%=			=%expansion=none ^
	-map 0:v ^
	-map 0:a? ^
	-c:a aac ^
	-q:a 1 ^
	-ac 1 ^
	-c:v h264 ^
	-crf 30 ^
	%VIDEO:~0,-5%_03.mp4"