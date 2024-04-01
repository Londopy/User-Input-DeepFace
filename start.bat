@echo off
pip install -r requirements.txt
sleep 1
python main.py %*
pause
