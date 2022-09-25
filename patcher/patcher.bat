:startup

@echo off
title startup

:admin

fltmc >nul 2>&1 && (
  echo has admin permissions
  PING localhost -n 2 >NUL
  cls
) || (
  echo has NOT admin permissions
  PING localhost -n 2 >NUL
  cls
  set /p = Please re-launch the program with Administrative permissions...!
  exit
)
SET /p = "Press any key to continue...!"


:shell

echo if you get any errors this is because the filepath doesnt exist or the script has to be updated

for /D %%I in ("%LOCALAPPDATA%\whatever\Versions\version-*") do cd /D "%%I"

call "%~dp0\winhttpjs.bat" "https://github.com/lolmanurfunny/Roblox-Launcher-minus-the-app/raw/main/RobloxPlayerLauncher.exe"

pause>NUL