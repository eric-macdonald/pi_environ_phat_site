from flask import Flask, render_template
import subprocess
import os
from datetime import datetime
from envirophat import weather
from envirophat import light
from envirophat import analog
from envirophat import leds

LEDout = False

app = Flask(__name__)

@app.route("/")
def check():
    global LEDout 
    if(LEDout):
        LEDout = False
        leds.off()
    else:
        LEDout = True
        leds.on()
#    tempString = os.popen('/opt/vc/bin/vcgencmd measure_temp').read()
    red, green, blue = light.rgb()
#    direction = motion.heading()
    analog0 = analog.read(0)
    analog1 = analog.read(1)
    analog2 = analog.read(2)
    analog3 = analog.read(3)
    tempString  = "Youngstown State University Environmental Sensing"
    tempString  = tempString + "\n" + str(datetime.now()) 
    tempString  = tempString + "\nTemperature = " +str(int(weather.temperature())) + " degrees Celsius"
    tempString  = tempString + ", \nPressure = " + str(int((weather.pressure(unit='hPa')))) + " hPa"
    tempString  = tempString + ", \nLight = " + str(int((light.light()))) 
    tempString  = tempString + ", \nRed light = " + str(red) 
    tempString  = tempString + ", \nGreen light = " + str(green) 
    tempString  = tempString + ", \nBlue light = " + str(blue) 
    tempString  = tempString + ", \nAnalog line zero = " + str(analog0) 
    tempString  = tempString + ", \nAnalog line one = " + str(analog1) 
    tempString  = tempString + ", \nAnalog line two = " + str(analog2) 
    tempString  = tempString + ", \nAnalog line three = " + str(analog3) 
    return  "<xmp>" + tempString  + "</xmp>"

if __name__ == "__main__":
       app.run(host='0.0.0.0', port=5000, debug=True)

