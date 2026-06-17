@echo off
cd /d "%~dp0"
del /s /q __pycache__\* 2>nul
ndel /s /q *.pyc 2>nul
nrd /s /q __pycache__ 2>nul
nrd /s /q .pytest_cache 2>nul
ndel /s /q .pytest_cache\* 2>nul
nrd /s /q dist 2>nul
nrd /s /q build 2>nul
nrd /s /q .venv 2>nul
necho Repo cleaned.
pause
