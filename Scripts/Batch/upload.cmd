@echo off
setlocal
copy Web\index.php C:\MAMP\htdocs\
Xcopy Audio\WAV_Formats C:\MAMP\htdocs\Audio\WAV_Formats /E /H /C /I