#! /usr/bin/bash
pyinstaller --onefile -n kuz main.py
chmod +x ./dist/kuz
sudo cp ./dist/kuz /usr/bin/