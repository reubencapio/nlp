tasklist /FI "IMAGENAME eq chrome.exe" /NH | find /I /N "chrome.exe">NUL 
IF /I "%ERRORLEVEL%" EQU "0" (
    ECHO chrome found
)
