@echo off
pip install -r requirements.txt
SLEEP 1
python main.py %*
pause
