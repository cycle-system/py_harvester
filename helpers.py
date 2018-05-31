# helpers file containing block-level functions used in main

from stm32Helper import STMBoard
from watsonHelper import Watson

stmBoard = STMBoard()
watson = Watson()

def getEnergyData():
    response = stmBoard.getMeasures()
    return response
    
def sendToWatson(eventName, data):
    watson.publishEvent(eventName, data)
