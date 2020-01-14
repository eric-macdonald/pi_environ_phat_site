Environ-phat web server

pip3 install -U flask

sudo apt-get install pimoroni
sudo apt-get install python3-envirophat

Update the "crontab -e"

Add this line to the end:
@reboot python /home/pi/environ_phat_site/environ_phat_site.py &
