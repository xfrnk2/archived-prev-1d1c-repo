echo >/dev/null # >nul & GOTO WINDOWS & rem ^\n
echo 'Processing for Linux'\n
@echo 'Processing for Linux'\n
\n
# ***********************************************************
# * NOTE: If you modify this content, be sure to remove carriage returns (\r) 
# *       from the Linux part and leave them in together with the line feeds 
# *       (\n) for the Windows part. In summary:
# *           New lines in Linux: \n
# *           New lines in Windows: \r\n 
# ***********************************************************
\n
# Do Linux Bash commands here... for example:
StartDir="$(pwd)"
\n
VENV ?= . venv/bin/activate
\n
# Then, when all Linux commands are complete, end the script with 'exit'...
exit 0
\n
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

:WINDOWS\r\n
@echo "Processing for Windows"\r\n
echo "Processing for Windows"\r\n
\r\n
REM Do Windows CMD commands here... for example:
SET StartDir=%cd%
\r\n
VENV ?= ..\venv\Scripts\activate.bat
\r\n

REM Then, when all Windows commands are complete... the script is done.