@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
for %%F in (0688244907*.pdf) do (
  rem echo %%F
  SET factura=%%F
  SET factura=!factura:~10,4!.!factura:~14,2!.!factura:~16,2!.pdf
  echo Renombrando %%F como !factura!
  ren %%F !factura!
)