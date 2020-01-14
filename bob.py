from envirophat import weather
from datetime import datetime

bob  = str(datetime.now()) + " " +str(weather.temperature()) + " " + str(weather.pressure(unit='hPa'))
print(bob)
