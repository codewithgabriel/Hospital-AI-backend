@echo off

:: Print Python version requirement message
echo Python 3.11.X is required to run this program.

:: Get the Python version
for /f "delims=" %%i in ('python --version') do set PYTHON_VERSION=%%i

:: Check if Python 3.11.X is installed
echo %PYTHON_VERSION% | findstr /r "3\.11\.[0-9]" >nul
if %ERRORLEVEL% neq 0 (
    echo ERROR: Python 3.11.X is not installed or not in PATH.
    echo Please install Python 3.11.X to continue.
    exit /b 1
)

:: Install the required Python packages
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to install dependencies. Please check the error message above.
    exit /b 1
)

:: Run the Flask app
echo Starting Flask server...
flask run --host=0.0.0.0 --port=8090

