# Harvester Energy Measuring

import helpers
from time import sleep

sleepTime = 1           # seconds
eventName = "energy-values"   # the name of the event as registered on the cloud

# main program
def __main__():
    while True:

        # read the energy measures data from the stm32 board
        energyData = helpers.getEnergyData()
        
        # send to cloud service
        if energyData is not None:
            helpers.sendToWatson(eventName, energyData)
        
        # sleep
        sleep(sleepTime)    
    
if __name__ == '__main__':
    __main__()
