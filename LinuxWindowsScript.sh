echo >/dev/null # >nul & GOTO WINDOWS & rem ^
echo 'Processing for Linux'

# ***********************************************************
# * NOTE: If you modify this content, be sure to remove carriage returns (\r) 
# *       from the Linux part and leave them in together with the line feeds 
# *       (\n) for the Windows part. In summary:
# *           New lines in Linux: \n
# *           New lines in Windows: \r\n 
# ***********************************************************

# Do Linux Bash commands here... for example:
StartDir="$(pwd)"
PATH_NAME= . venv/bin/activate
#VENV ?= . venv/bin/activate
# Then, when all Linux commands are complete, end the script with 'exit'...
echo $(PATH_NAME)
export $(PATH_NAME)

exit 0

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

:WINDOWS
echo "Processing for Windows"

REM Do Windows CMD commands here... for example:
SET StartDir=%cd%
VENV ?= . venv/Scripts/activate.bat 
REM Then, when all Windows commands are complete... the script is done.