## test script

# OZY v0.2

### install google-chrome v98 on server:
```sh
# chrome v98.0
sudo dpkg -i chrome_96_x64.deb
sudo apt install -y -f
sudo google-chrome --version
# if needed to remove:
# apt remove google-chrome
```

### to run:
```sh
python3 -m venv .env
. ./.env/bin/activate
pip install -r requirements.txt
python3 main.py
```

