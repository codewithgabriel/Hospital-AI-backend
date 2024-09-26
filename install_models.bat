@echo off
echo "Installing dependencies.."
pip install transformers 
echo "Installing Translator models..."
python models/nupe_to_eng.py
python models/nupe_yor.py 
python models/yor_to_eng.py 



