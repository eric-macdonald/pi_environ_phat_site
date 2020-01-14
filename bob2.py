from flask import Flask, render_template
import subprocess
import os
from datetime import datetime
import datetime
import time
from envirophat import weather
app = Flask(__name__)

@app.route("/")
def hello():
#    tempString = os.popen('/opt/vc/bin/vcgencmd measure_temp').read()
    tempString  = datetime.now() + " " +str(weather.temperature()) + " " + str(weather.pressure(unit='hPa'))
    #tempString  = str(weather.temperature()) + " " + str(weather.pressure(unit='hPa'))
    return tempString

if __name__ == "__main__":
       app.run(host='0.0.0.0', port=5000, debug=True)

