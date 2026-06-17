@echo off
cd /d "%~dp0"
python -m pylint main.py src tests
pause
